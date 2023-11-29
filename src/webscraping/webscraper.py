from src.webscraping.basecrawler import BaseCrawler
from ..util.crawling_util import create_driver

from src.webscraping.coupang_webcrawler import Coupang
from src.webscraping.ssg_webcrawler import Ssg
from src.webscraping.gsshop_webcrawler import Gsshop
from src.webscraping.naver_webcrawler import Naver

import pymysql
import os
from src.util.db_util import get_db_connection
from src.database.query import create_product_info_table_query, update_product_info_query

from src.product.get_nutri_data import GetNutriData as nd

class WebScraper(BaseCrawler):

    last_batch_file = 'src/logs/last_batch.txt'


    #크롤링 서버 돌아가다가 중단 되어도 마지막 작업 했던 구간부터 이어서 돌릴 수 있게끔 파일시스템에 마지막 batch_size 저장.
    @classmethod
    def save_last_batch_index(cls, batch_index):
        with open(cls.last_batch_file, 'w') as file:
            file.write(str(batch_index))

    @classmethod
    def get_last_batch_index(cls):
        if os.path.exists(cls.last_batch_file):
            with open(cls.last_batch_file, 'r') as file:
                value = file.read().strip()
                if value: # 비어있지 않은 경우
                    return int(value) 
                else: 0
        return 0
            

    @staticmethod
    def get_image_from_naver(product_to_search):

        #네이버쇼핑에서 이미지만 얻어오기
        naver_instance = Naver(product_to_search)
        image_url = naver_instance.webcrawler()

        if image_url:
            return image_url
        else:
            return None

    @classmethod    
    def get_data_from_site(cls):

        data_list = nd.fetch_json_data_from_file()
        BATCH_SIZE = 5

        # data_list의 전체길이를 BATCH_SIZE로 나누어 몇개의 batch로 나눌 수 있는지 계산한다. 
        # 사실상 데이터의 총 갯수가 5만개이므로 BATCH_SIZE가 10인 경우 total_batches 는 5천이다. 
        total_batches = len(data_list) // BATCH_SIZE + (1 if len(data_list) % BATCH_SIZE >0 else 0)

        #마지막 batch_size 저장, 서버 돌릴 때 작업 이어서 할 수 있게 하기
        last_batch = cls.get_last_batch_index()

        # for batch in range(total_batches):
        for batch in range(last_batch, total_batches):

            conn = get_db_connection()
            cur = conn.cursor()
            # cur.execute(create_product_info_table_query)

            try:
                #지정한 batch_size 만큼의 상품을 검색

                #현재 batch의 시작 인덱스 계산
                start_index = batch * BATCH_SIZE
                #data_list의 길이를 넘어가지 않아야 한다. 
                end_index = min((batch+1) * BATCH_SIZE, len(data_list))

                ssg_list = []
                coupang_list = []
                gs_list = []

                for data in data_list[start_index:end_index]:

                    product_id = int(nd.clean_code(data['식품코드']))
                    product_to_search = nd.clean_name(data['식품명'])

                    #가격, 이미지 데이터 크롤링
                    crawler = BaseCrawler(product_id, product_to_search)

                    #부모 클래스에서 정의한 메서드 
                    gs_product_info_tuple = crawler.get_product_info(Gsshop, product_id, product_to_search)
                    gs_list.append(gs_product_info_tuple)

                    coupang_product_info_tuple = crawler.get_product_info(Coupang, product_id, product_to_search)
                    coupang_list.append(coupang_product_info_tuple)

                    ssg_product_info_tuple = crawler.get_product_info(Ssg, product_id, product_to_search)
                    ssg_list.append(ssg_product_info_tuple)


                cur.executemany(update_product_info_query, ssg_list)
                cur.executemany(update_product_info_query, coupang_list)
                cur.executemany(update_product_info_query, gs_list)

                conn.commit()
                print(f"Current batch {batch}: Successfully inserted records to database")

            except pymysql.Error as error:
                print(f"Current batch {batch}: Failed to insert records to database: {error}")
                conn.rollback()
            
            finally:
                # 성공적으로 commit 된 경우에만 마지막 batch 저장
                cls.save_last_batch_index(batch)

                cur.close
                conn.close()
                print("MySQL connection is closed")