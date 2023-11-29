import os 
from dotenv import load_dotenv

load_dotenv()

#Naver Cloud
S3_CONFIG = {
    'service_name' : os.getenv('SERVICE_NAME'),
    'access_key': os.getenv('ACCESS_KEY'),
    'secret_key': os.getenv('SECRET_KEY'),
    'region_name': os.getenv('REGION_NAME'),
    'endpoint_url': os.getenv('ENDPOINT_URL'),
    'bucket_name': os.getenv('BUCKET_NAME'),
    'folder_name': os.getenv('FOLDER_NAME')
}

