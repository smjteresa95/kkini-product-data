from src.webscraping.coupang_webcrawler import Coupang
from src.webscraping.ssg_webcrawler import Ssg

from src.product.get_nutri_data import GetNutriData as nd

data_list = nd.fetch_json_data_from_file()

ssg_list = []

for data in data_list:
    product_id = int(nd.clean_code(data['식품코드']))
    product_to_search = nd.clean_name(data['식품명'])
 
    ssg_instance = Ssg(product_id, product_to_search)
    product_info = ssg_instance.ssg_crawler()
    #각 ProductInfo 객체의 필요한 데이터를 튜플 형식으로 저장한다.
    #객체에서 attribute 얻어 올 때 getattr() 사용한다. 
    ssg_product_info = (product_id,
                        getattr(product_info, 'product_link', None), 
                        getattr(product_info, 'site', None), 
                        getattr(product_info, 'product_img', None),
                        getattr(product_info, 'original_price', None), 
                        getattr(product_info, 'sales_price', None), 
                        getattr(product_info, 'discount_rate', None)
                        )
    ssg_list.append(ssg_product_info)