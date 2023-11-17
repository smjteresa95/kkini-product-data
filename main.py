from src.product.parse_data import SaveProduct as sp
from src.productfilter.save_nutri_filter import SaveNutriFilter as nf
from src.product.save_product_image import SaveProductImage as gi

if __name__ == '__main__':

    # DB에 기준일 이후의 공공데이터 저장 
    # sp.insert_sql_from_json('2023-08-09')

    # #product filter
    # filter = nf()
    # filter.fill_filter_column()

    #이미지 url 저장
    gi.get_image_upload_to_s3()




