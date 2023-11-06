import re 
from ..util.crawling_util import create_driver

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from ..webscraping.productinfo import ProductInfo

class Ssg:

    def __init__(self, product_id, product_to_search):
        self.product_id = product_id
        self.product_to_search = product_to_search

    def ssg_crawler(self):
        driver = create_driver()

        search_url = 'https://www.ssg.com/search.ssg?target=all&query='
        url = search_url + self.product_to_search
 
        driver.get(url)

        # product_info_list = []
        product_id = self.product_id
        site = 'ssg'
        product_img = None
        product_link = None
        original_price = None
        sales_price = None
        discount_rate = None
        
        try:
            name_elements = driver.find_elements(By.CLASS_NAME, "title")
            name_list = [name_elements[i].text.replace(" ", "") for i in range(min(5, len(name_elements)))]

            product_name = self.product_to_search.replace(" ","")
            contains_name = [] #인덱스와 일치하는 상품명 저장할 리스트

            for index, s in enumerate(name_list):
                if product_name in s:
                    contains_name.append((index, s))
                    

            # Check if we have any product names that matched
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
            index = contains_name[0][0]+1

            #제품링크
            link_xpath = f"//ul/li[{index}]/div[1]/div[2]/a"
            link_element = driver.find_element(By.XPATH, link_xpath)
            product_link = link_element.get_attribute('href') # 해당 index 요소의 'href'속성값을 가져온다.
            # product_info_list.append(product_link)
            print(product_link)

            #제품상세페이지로 이동 
            driver.get(product_link)

            #제품이미지
            img_element = driver.find_element(By.ID, 'mainImg')
            product_img = img_element.get_attribute('src')
            # product_info_list.append(product_img)
            print(product_img)

            #할인 전 금액
            try:
                original_price_xpath = "//span[contains(@class, 'cdtl_old_price')]/em[contains(@class, 'ssg_price')]"
                original_price_element = driver.find_element(By.XPATH, original_price_xpath)
                original_price = int(re.sub('[,원]','', original_price_element.text))
                # product_info_list.append(original_price)
                print(original_price)
            except NoSuchElementException:
                # product_info_list.append(None)
                print("None")

            #할인 후 금액
            try:
                sales_price_xpath = "//span[contains(@class, 'cdtl_new_price') and contains(@class, 'notranslate')]/em[contains(@class, 'ssg_price')]"
                sales_price_element = driver.find_element(By.XPATH, sales_price_xpath)
                sales_price = int(sales_price_element.text.replace(',','').strip())
                # product_info_list.append(sales_price)
                print(sales_price)
            except NoSuchElementException:
                # product_info_list.append(None)
                print("None")

            #할인률
            try:
                discount_rate_xpath = "//span[contains(@class, 'cdtl_new_price') and contains(@class, 'notranslate')]/em[contains(@class, 'ssg_percent')]"
                discount_rate_element = driver.find_element(By.XPATH, discount_rate_xpath)
                discount_rate = int(discount_rate_element.text.replace('%','').strip())
                # product_info_list.append(discount_rate)
                print(discount_rate)
            except NoSuchElementException:
                # product_info_list.append(None)
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

        

        
       
        



        

        






