from src.webscraping.basecrawler import BaseCrawler
from ..util.crawling_util import create_driver

from src.webscraping.coupang_webcrawler import Coupang
from src.webscraping.ssg_webcrawler import Ssg
from src.webscraping.gsshop_webcrawler import Gsshop
from src.webscraping.naver_webcrawler import Naver

import pymysql
from src.util.db_util import get_db_connection
from src.database.query import create_product_info_table_query, update_product_info_query

from src.product.get_nutri_data import GetNutriData as nd

class WebScraper(BaseCrawler):

    @staticmethod
    def get_image_from_naver(product_to_search):

        #네이버쇼핑에서 이미지만 얻어오기
        naver_instance = Naver(product_to_search)
        image_url = naver_instance.webcrawler()

        if image_url:
            return image_url
        else:
            return None

    def get_data_from_site():

        data_list = nd.fetch_json_data_from_file()

        # conn = get_db_connection()
        # cur = conn.cursor()
        # cur.execute(create_product_info_table_query)

        ssg_list = []
        coupang_list = []
        gs_list = []
        img_list = []

        for data in data_list:

            product_id = int(nd.clean_code(data['식품코드']))
            product_to_search = nd.clean_name(data['식품명'])
            
            #네이버쇼핑에서 이미지만 얻어오기
            naver_instance = Naver(product_to_search)
            img_tuple = (product_id, naver_instance.webcrawler())
            print(naver_instance.webcrawler())
            img_list.append(img_tuple)

            # #가격, 이미지 데이터 크롤링
            # crawler = BaseCrawler(product_id, product_to_search)

            # #부모 클래스에서 정의한 메서드 
            # gs_product_info_tuple = crawler.get_product_info(Gsshop, product_id, product_to_search)
            # gs_list.append(gs_product_info_tuple)

            # coupang_product_info_tuple = crawler.get_product_info(Coupang, product_id, product_to_search)
            # coupang_list.append(coupang_product_info_tuple)

            # ssg_product_info_tuple = crawler.get_product_info(Ssg, product_id, product_to_search)
            # ssg_list.append(ssg_product_info_tuple)


        # try:
        #     cur.executemany(update_product_info_query, ssg_list)
        #     conn.commit()
        #     print("Successfully inserted records to database")

        # except pymysql.Error as error:
        #     print("Failed to insert records to database: {}".format(error))
        
        # conn.close()
            # print("MySQL connection is closed")