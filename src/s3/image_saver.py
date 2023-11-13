import boto3
import requests
from io import BytesIO

from src.config.s3_config import S3_CONFIG

class ImageSaver:

    bucket_name = 'kkini-image-bucket'
    folder_name = 'product-image'

    # AWS
    # s3 = boto3.client(
    #     service_name = S3_CONFIG['service_name'],
    #     region_name = S3_CONFIG['region_name'],
    #     aws_access_key_id = S3_CONFIG['access_key'],
    #     aws_secret_access_key = S3_CONFIG['secret_key']
    # )
    
    #Naver Cloud
    s3 = boto3.client(
        service_name = S3_CONFIG['service_name'],
        endpoint_url = S3_CONFIG['endpoint_url'],
        # region_name = S3_CONFIG['region_name'],
        aws_access_key_id = S3_CONFIG['access_key'],
        aws_secret_access_key = S3_CONFIG['secret_key']
    )

    @classmethod
    def get_buckets(cls):
        response = cls.s3.list_buckets()
        for bucket in response.get('Buckets', []):
            print(bucket.get('Name'))

    @classmethod
    def download_image(cls, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            return BytesIO(response.content)
        else:
            return None

    #사진명(object_name, file_name)은 제품명으로 저장

    #file_name 에는 data['제품명']을,
    #image_obj에는 download_image 메서드로 채우면 된다.
    @classmethod
    def upload_to_s3(cls, file_name, image_obj):
        object_name = f'{cls.folder_name}/{file_name}.jpg'
        cls.s3.upload_fileobj(image_obj, cls.bucket_name, object_name)

    @classmethod
    def get_public_url(cls, file_name):
        object_name = f'{cls.folder_name}/{file_name}.jpg'
        #public access가능하도록 권한설정
        cls.s3.put_object_acl(Bucket=cls.bucket_name, Key=object_name, ACL='public-read')
        return f"{S3_CONFIG['endpoint_url']}/{cls.bucket_name}/{object_name}"

