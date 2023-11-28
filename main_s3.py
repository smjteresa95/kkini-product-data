#이미지 S3에 저장 테스트 파일(삭제해도 무방)
from src.s3.image_saver import ImageSaver

image_url = 'https://shopping-phinf.pstatic.net/main_5716183/5716183724.20210713112326.jpg?type=f640'
#same as product_name
file_name = '팔도비빔면'

#크롤링 한 이미지 url로 객체생성
image_content = ImageSaver.download_image(image_url)

#객체를 object storage 에 저장
if image_content:
    ImageSaver.upload_to_s3(file_name, image_content)
    print('image successfully updated to the object storage')

#url 얻어오기
print(ImageSaver.get_public_url(file_name))