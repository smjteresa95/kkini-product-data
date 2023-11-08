from ..util.crawling_util import create_driver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from ..webscraping.productinfo import ProductInfo

class Coupang:

    def __init__(self, product_id, product_to_search):
        self.product_id = product_id
        self.product_to_search = product_to_search

    def webcrawler(self):

        driver = create_driver()

        search_url = "https://www.coupang.com/np/search?component=&q="
        url = search_url + self.product_to_search

        driver.get(url)

        product_id = self.product_id
        site = 'coupang'
        product_img = None #쿠팡에서는 이미지를 가지고 올 수 없으므로 항상 None
        product_link = None
        original_price = None
        sales_price = None
        discount_rate = None

        try:
            #상품명
            name_elements = driver.find_elements(By.CLASS_NAME, "name")
            name_list = [name_elements[i].text.replace(" ", "") for i in range(min(5, len(name_elements)))] #요소의 텍스트를 가져오고 공백을 제거한다. 

            product_name = self.product_to_search.replace(" ","")
            contains_name = [] #인덱스와 일치하는 상품명 저장할 리스트

            for index, s in enumerate(name_list):
                if product_name in s:
                    contains_name.append((index, s))
            
            # Check if we have any product names that matched
            if not contains_name:
                print("No products found matching the search criteria.")
                return ProductInfo(
                    product_id=product_id,
                    site=site,
                    product_img=product_img,
                    original_price=original_price,
                    sales_price=sales_price,
                    discount_rate=discount_rate
                )

            index = contains_name[0][0] 

            #상품링크
            link_elements = driver.find_elements(By.CLASS_NAME, "search-product-link")
            product_link = link_elements[index].get_attribute('href') # 해당 index 요소의 'href'속성값을 가져온다.
            print(product_link)

            #할인 전 금액
            try:
                original_price_elements = driver.find_elements(By.CLASS_NAME, "base-price")
                original_price = int(original_price_elements[index].text.replace(",",""))
                print(original_price)
            except NoSuchElementException:
                print("None")

            #할인 후 금액
            try:
                sales_price_elements = driver.find_elements(By.CLASS_NAME, "price-value")
                sales_price = int(sales_price_elements[index].text.replace(",",""))
                print(sales_price)
            except NoSuchElementException:
                print("None")

            #할인률
            try:
                discount_rate_elements = driver.find_elements(By.CLASS_NAME, "instant-discount-rate")
                discount_rate = int(discount_rate_elements[index].text.replace("%",""))
                print(discount_rate)
            except NoSuchElementException:
                print("None")

            
            driver.close()
            return ProductInfo(
                product_id=product_id,
                site=site,
                product_link=product_link,
                original_price=original_price,
                sales_price=sales_price,
                discount_rate=discount_rate
            )

        except Exception as e:
            print(f"검색결과가 없습니다: {e}")


