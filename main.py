from src.product.parse_data import SaveProduct as sp
from src.productfilter.save_nutri_filter import SaveNutriFilter as nf

if __name__ == '__main__':

    # #DB에 기준일 이후의 공공데이터 저장 
    sp.insert_sql_from_json('2023-08-09')

    #product filte
    # filter = nf()
    # filter.fill_filter_column()


