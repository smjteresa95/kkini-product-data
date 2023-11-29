from src.product.parse_data import SaveProduct as sp
from src.productfilter.save_nutri_filter import SaveNutriFilter as nf
from src.product.save_product_image import SaveProductImage as gi
from src.webscraping.webscraper import WebScraper

if __name__ == '__main__':

    # DB에 기준일 이후의 공공데이터 저장 
    # sp.insert_sql_from_json('2023-08-09')

    # #product filter
    # filter = nf()
    # filter.fill_filter_column()

    # 웹 스크래핑 해서 product_info 테이블 채우기
    WebScraper.get_data_from_site()

    #네이버에서 크롤링한 이미지 S3에 저장 후 DB에 public url 저장
    # gi.get_image_upload_to_s3()




