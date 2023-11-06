#json파일에서 필요한 데이터들을 DB의 product 테이블에 저장
import pymysql

from src.database.db_util import get_db_connection
from src.database.query import update_product_from_public_data_query, create_product_table_query

from src.nutridata.get_nutri_data import GetNutriData as nd
from src.productfilter.cal_nutri_filter import CalNutriFilter as nf

class SaveProduct:

    #cutoff_date 이후의 데이터만 DB에 저장. 
    def insert_sql_from_json(cutoff_date):

        #공공데이터 가지고 오기
        data_list = nd.fetch_json_data_from_file()

        #데이터 기준 일자가 특정일 이후인 데이터들만 가지고 오게하기.
        #식품코드가 동일하면 update, 다르면 insert
        cutoff_date = nd.convert_to_date(cutoff_date)

        #dictionary에서 필요한 필드들만 빼서 tuple로 변환. for bulk update.
        product_data = []

        for data in data_list:

            category = nd.set_category(data)
            kcal = data['에너지(kcal)']
            carb =  data['탄수화물(g)']
            protein = data['단백질(g)']
            fat = data['지방(g)']
            sodium = data['나트륨(mg)']
            cholesterol = data['콜레스테롤(mg)']
            sat_fat = data['포화지방산(g)']
            trans_fat = data['트랜스지방산(g)']
            sugar = data['당류(g)']
    
            #is_green
            cal_nutri_filter_instance = nf(
                category = category,
                kcal = kcal,
                carb = carb,
                protein = protein,
                fat = fat,
                sodium = sodium,
                cholesterol = cholesterol,
                sat_fat = sat_fat,
                trans_fat = trans_fat,
                sugar = sugar
            )

            is_green = cal_nutri_filter_instance.get_is_green()

            nut_score = cal_nutri_filter_instance.get_nut_score()

            if nd.convert_to_date(data['데이터기준일자']) >= cutoff_date:
                product_data.append([nd.clean_code(data['식품코드']), nd.clean_name(data['식품명']), nd.get_brand(data), category, data['식품대분류명'], data['식품중분류명'], data['식품소분류명'], 
                                    data['식품중량'], nd.subtract_unit(data['영양성분함량기준량']), data['1회 섭취참고량'], kcal, 
                                   carb, protein, fat, sodium, cholesterol, sat_fat, trans_fat, sugar, is_green, nut_score])
                                
        
        #Mysql연결
        conn = get_db_connection()

        #sql 쿼리 실행해주고 결과 반환 해 줄 커서객체 생성
        cur = conn.cursor()

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


                

