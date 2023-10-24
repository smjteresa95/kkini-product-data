#json파일에서 필요한 데이터들을 DB에 저장
import json
import pymysql
from datetime import datetime

from src.config.db_config import DB_CONFIG, DATA_PATH
from src.database.query import update_product_from_public_data_query


#데이터에 들어있는 문자 제거.
def subtract_g(value):
    #단위g을 삭제
    return value.replace('g','').strip()


#상품명 앞 카테고리 붙는거 삭제
def clean_data(value):
    #_를 기준으로 나누고, 맨 앞 요소(카테고리명) 삭제, 문자열로 변환
    return ''.join(value.split('_')[1:])


#문자열을 날짜 객체로 변경 strptime
def convert_to_date(value):
    return datetime.strptime(value, '%Y-%m-%d').date()


#cutoff_date 이후의 데이터만 DB에 저장. 
def insert_sql_from_json(cutoff_date):

    #Mysql연결
    conn = pymysql.connect(
        host=DB_CONFIG['host'],
        user=DB_CONFIG['user'],
        password=DB_CONFIG['password'],
        database=DB_CONFIG['database'],
        charset='utf8'
    )

    #sql 쿼리 실행해주고 결과 반환 해 줄 커서객체 생성
    cur = conn.cursor()

    #공공데이터 가지고 오기
    with open(DATA_PATH, encoding="utf8") as f:
        json_data = json.load(f) 

        #TODO
        #데이터 기준 일자가 특정일 이후인 데이터들만 가지고 오게하기.
        #식품코드가 동일하면 update, 다르면 insert
        cutoff_date = convert_to_date(cutoff_date)

        data_list = json_data["records"]

        #dictionary에서 필요한 필드들만 빼서 tuple로 변환. for bulk update.
        product_data = [(data['식품코드'], clean_data(data['식품명']), data['제조사명'], data['식품소분류명'], data['식품대분류명'], 
                         subtract_g(data['식품중량']), subtract_g(data['1회 섭취참고량']), subtract_g(data['영양성분함량기준량']), data['에너지(kcal)'], 
                         data['탄수화물(g)'], data['단백질(g)'], data['지방(g)'], data['나트륨(mg)'], 
                         data['콜레스테롤(mg)'], data['포화지방산(g)'], data['트랜스지방산(g)'], data['당류(g)']) 
                        for data in data_list if convert_to_date(data['데이터기준일자']) >= cutoff_date]
        
        try:
            cur.executemany(update_product_from_public_data_query, product_data)
            conn.commit()

        except pymysql.Error as error:
            print("Failed to insert records to database: {}".format(error))

        finally:
            conn.close()
            print("MySQL connection is closed")


            

