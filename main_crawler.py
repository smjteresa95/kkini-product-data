from src.webscraping.webscraper import WebScraper
from src.product.get_nutri_data import GetNutriData as nd

WebScraper.get_data_from_site()
# WebScraper.get_image_from_naver()

# data_list = nd.fetch_json_data_from_file()
# for data in data_list:
#     product_to_search = nd.clean_name(data['식품명'])
#     image_url = WebScraper.get_image_from_naver(product_to_search)
