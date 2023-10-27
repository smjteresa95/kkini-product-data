#json파일에서 필요한 데이터들을 DB에 저장
import pymysql
from datetime import datetime
import re #정규표현식을 쓰기 위한 Lib

from src.database.db_util import get_db_connection
from src.database.query import update_product_from_public_data_query, create_product_table_query

from src.nutridata.get_nutri_data import GetNutriData as nd

def clean_code(value):
    #정규표현식 이용해서 product code 앞 P와 -삭제하고 int형으로 변환
    return int(re.sub('[P-]','',value))


#상품명 앞 카테고리 붙는거 삭제
def clean_data(value):
    #_를 기준으로 나누고, 맨 앞 요소(카테고리명) 삭제, 문자열로 변환
    return ''.join(value.split('_')[1:])


#문자열을 날짜 객체로 변경 strptime
def convert_to_date(value):
    return datetime.strptime(value, '%Y-%m-%d').date()

# 유통업체를 brand column에 넣되, 유통업체가 '해당없음'이면 '제조사명'에 해당하는 값 넣기. 둘 다 없으면 '정보없음' 넣어주기
def get_brand(data):
    if data['유통업체명'] != '해당없음':  
        return data['유통업체명']
    elif data['유통업체명'] != '해당없음': 
        return data['제조사명']
    else:
        return '정보없음'


#cutoff_date 이후의 데이터만 DB에 저장. 
def insert_sql_from_json(cutoff_date):

    #Mysql연결
    conn = get_db_connection()

    #sql 쿼리 실행해주고 결과 반환 해 줄 커서객체 생성
    cur = conn.cursor()

    #공공데이터 가지고 오기
    data_list = nd.fetch_json_data_from_file()

    #데이터 기준 일자가 특정일 이후인 데이터들만 가지고 오게하기.
    #식품코드가 동일하면 update, 다르면 insert
    cutoff_date = convert_to_date(cutoff_date)

    #dictionary에서 필요한 필드들만 빼서 tuple로 변환. for bulk update.
    product_data = [(clean_code(data['식품코드']), clean_data(data['식품명']), get_brand(data), nd.set_category(data), data['식품대분류명'], data['식품중분류명'], data['식품소분류명'], 
                        nd.subtract_g(data['식품중량']), nd.subtract_g(data['1회 섭취참고량']), data['에너지(kcal)'], 
                        data['탄수화물(g)'], data['단백질(g)'], data['지방(g)'], data['나트륨(mg)'], 
                        data['콜레스테롤(mg)'], data['포화지방산(g)'], data['트랜스지방산(g)'], data['당류(g)']) 
                    for data in data_list if convert_to_date(data['데이터기준일자']) >= cutoff_date]
    
    try:
        cur.execute(create_product_table_query)
        cur.executemany(update_product_from_public_data_query, product_data)
        conn.commit()
        print("Successfully inserted records to database")

    except pymysql.Error as error:
        print("Failed to insert records to database: {}".format(error))

    finally:
        conn.close()
        print("MySQL connection is closed")


            

