from src.product.get_nutri_data import GetNutriData as nd
from src.productfilter.cal_nutri_filter import CalNutriFilter as nf

import pymysql
from src.util.db_util import get_db_connection
from src.database.query import update_filter_query, create_filter_table_query

class SaveNutriFilter:

    def get_filter_list(self):

        nutri_data = nd.fetch_json_data_from_file()

        all_filter = []

        for data in nutri_data:
            product_code = nd.clean_code(data['식품코드'])
            product_name = nd.clean_name(data['식품명'])
            category = nd.set_category(data)

            filter_instance = nf(category, float(data['에너지(kcal)']), float(data['탄수화물(g)']), float(data['단백질(g)']), 
                                 float(data['지방(g)']), float(data['나트륨(mg)']), float(data['콜레스테롤(mg)']), 
                                 float(data['포화지방산(g)']), float(data['트랜스지방산(g)']), float(data['당류(g)']))
            
            nutri_filter = filter_instance.get_nutri_filter()
            combined_filter = [product_code, product_name, category] + nutri_filter

            all_filter.append(combined_filter)
        
        return all_filter
    

    def fill_filter_column(self):
        conn = get_db_connection()
        cur = conn.cursor()

        filter_list = self.get_filter_list()
        try:
            cur.execute(create_filter_table_query)
            cur.executemany(update_filter_query, filter_list)
            conn.commit()
            print("Successfully inserted records to database")

        except pymysql.Error as error:
            print("Failed to insert records to database: {}".format(error))

        finally:
            conn.close()
            print("MySQL connection is closed")



    


            


    


