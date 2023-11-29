import os 
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('HOST'),
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE')
}

#공공데이터 json 파일경로
DATA_PATH = os.getenv('DATA_PATH')