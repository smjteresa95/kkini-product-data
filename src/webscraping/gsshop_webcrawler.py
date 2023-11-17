from ..util.crawling_util import create_driver
from ..webscraping.basecrawler import BaseCrawler
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from ..webscraping.productinfo import ProductInfo

class Gsshop():

    def __init__(self, product_id, product_to_search):
        self.product_id = product_id
        self.product_to_search = product_to_search

    def webcrawler(self):

        driver = create_driver()

        search_url = "https://with.gsshop.com/shop/search/main.gs?lseq=392813&tq="
        url = search_url + self.product_to_search

        driver.get(url)

        product_id = self.product_id
        site = 'gs'
        product_img = None 
        product_link = None
        original_price = None
        sales_price = None
        discount_rate = None

        try:
            #상품명
            name_elements = driver.find_elements(By.CLASS_NAME, "prd-name")
            name_list = [name_elements[i].text.replace(" ", "") for i in range(min(5, len(name_elements)))]

            product_name = self.product_to_search.replace(" ","")
            contains_name = [] #인덱스와 일치하는 상품명 저장할 리스트

            for index, s in enumerate(name_list):
                if product_name in s:
                    contains_name.append((index, s))
                    
            # 검색결과가 없는 경우
            if not contains_name:
                print("No products found matching the search criteria.")
                # return [None]*5
                driver.close()
                return ProductInfo(product_id = product_id, 
                                site = site, 
                                product_link = product_link, 
                                product_img = product_img, 
                                original_price = original_price, 
                                sales_price = sales_price, 
                                discount_rate = discount_rate)

            print(contains_name[0][1])
            index = contains_name[0][0]

            #상품링크
            link_elements = driver.find_elements(By.CLASS_NAME, "prd-item")
            product_link = link_elements[index].get_attribute('href')
            print(product_link)

            driver.get(product_link)

            #이미지
            try: 
                img_xpath = "//a[@class='btn_img']/img"
                img_element = driver.find_element(By.XPATH, img_xpath)
                img = img_element.get_attribute('src')
                print(img)
            except NoSuchElementException:
                print("None")

            #할인 전 금액
            try:
                original_price_xpath = "//div[@class='price-info']/div[@class='price-big']/div[@class='price-definition']/div[@class='price-definition-upper']/del"
                original_price_element = driver.find_element(By.XPATH, original_price_xpath)
                original_price = int(original_price_element.text.replace(',', ''))
                print(original_price)
            except NoSuchElementException as e:
                print("None")
            
            #할인 후 금액
            try:
                sales_price_xpath = "//div[@class='price-definition-base']//span[@class='price-definition-ins']/ins/strong"
                sales_price_element = driver.find_element(By.XPATH, sales_price_xpath)
                sales_price = int(sales_price_element.text.replace(',', ''))
                print(sales_price)
            except NoSuchElementException as e:
                print("None")
            
            #할인률
            try:
                discount_rate_xpath = "//div[@class='price-definition-base']//span[@class='price-definition-percent']/em"
                discount_rate_element = driver.find_element(By.XPATH, discount_rate_xpath)
                discount_rate = int(discount_rate_element.text)
                print(discount_rate)
            except NoSuchElementException as e:
                print("None")
            
             # return product_info_list
            driver.close()
            return ProductInfo(product_id = product_id, 
                                site = site, 
                                product_link = product_link, 
                                product_img = product_img, 
                                original_price = original_price, 
                                sales_price = sales_price, 
                                discount_rate = discount_rate)


        except Exception as e:
            print(f"검색결과가 없습니다: {e}")

        

