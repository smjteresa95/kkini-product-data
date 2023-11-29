from src.webscraping.naver_webcrawler import Naver
from src.product.get_nutri_data import GetNutriData as nd
from src.s3.image_saver import ImageSaver

from src.util.db_util import get_db_connection
from src.database.query import update_product_image_url


class SaveProductImage:

    # product_info 테이블(크롤링 한 상품 데이터 담는 테이블)에서 가지고 온 image url을 
    # object storage에 저장하고, public url 만들어 반환하는 메서드
    @staticmethod
    def image_s3_uploader(product_name, image_url):
            
        #크롤링 한 이미지 url로 객체생성
        image_content = ImageSaver.download_image(image_url)
    
        #객체를 object storage 에 저장
        if image_content:
            ImageSaver.upload_to_s3(product_name, image_content)
            print('image successfully updated to the object storage')

        #url 얻어오기
        return ImageSaver.get_public_url(product_name)


    #네이버 쇼핑에서 크롤링 한 이미지 url을 object storage에 저장하고, public url 만들어 반환
    @classmethod
    def naver_image_s3_uploader(cls, file_name):

        #네이버에서 상품이미지를 찾을 수 있는 경우
        #파일이름은 상품명으로 한다.
        naver_instance = Naver(file_name)
        image_url = naver_instance.webcrawler()

        if image_url:

            #크롤링 한 이미지 url로 객체생성
            image_content = ImageSaver.download_image(image_url)

            #객체를 object storage 에 저장
            if image_content:
                ImageSaver.upload_to_s3(file_name, image_content)
                print('image successfully updated to the object storage')

            #url 얻어오기
            return ImageSaver.get_public_url(file_name)
        
        #상품 이미지 찾을 수 없는 경우 None return
        else:
            return None

    # naver_image_s3_uploader() 메서드를 전체 상품에 적용.
    @classmethod
    def get_naver_image_upload_to_s3(cls):
        
        data_list = nd.fetch_json_data_from_file()
        BATCH_SIZE = 10

        total_batches = len(data_list) // BATCH_SIZE + (1 if len(data_list) % BATCH_SIZE > 0 else 0)

        for batch in range(total_batches):

            conn = get_db_connection()
            cur = conn.cursor()

            try:
                #지정한 batch size 만큼의 상품을 검색 후 
                start_index = batch * BATCH_SIZE
                end_index = min((batch + 1) * BATCH_SIZE, len(data_list))

                for data in data_list[start_index:end_index]:

                    product_id = int(nd.clean_code(data['식품코드']))
                    product_name = nd.clean_name(data['식품명'])
                    public_url = None

                    try:
                        #이미지 object storage에 업로드,
                        public_url = cls.naver_image_s3_uploader(product_name)
                    except Exception as e:
                        print(f"이미지 object storage에 업로드: {e}")

                    if public_url:
                        #얻은 public url을 DB에 저장
                        cur.execute(update_product_image_url, (public_url, product_id))

                conn.commit()  # 모든 업데이트 후에 한 번만 커밋합니다.
                print("data has been commited to the database")

            except Exception as e:
                print(f"An error occurred: {e}")
                conn.rollback()

            finally:
                cur.close()
                conn.close() 



            





