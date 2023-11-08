from ..util.crawling_util import create_driver
from ..webscraping.basecrawler import BaseCrawler
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from ..webscraping.productinfo import ProductInfo

#네이버에서는 이미지만 받아올 예정.
class Naver():

    def __init__(self, product_id, product_to_search):
        self.product_id = product_id
        self.product_to_search = product_to_search

    def webcrawler(self):

        driver = create_driver()
        url = "https://msearch.shopping.naver.com/search/all?query=" + self.product_to_search
        driver.get(url)        

        try:
            #상품명
            name_elements = driver.find_elements(By.CLASS_NAME, "product_info_tit__c5_pb")
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
                return None

            print(contains_name[0][1])


            #첫번째 상품의 링크로 이동
            index = contains_name[0][0]
            #상품링크
            link_xpath = "//div[@class='product_info_main__piyRs']/a"
            link_elements = driver.find_elements(By.XPATH, link_xpath)

            product_link = link_elements[index].get_attribute('href')
            driver.get(product_link)

            #이미지
            try: 
                img_element = driver.find_element(By.CLASS_NAME, "simpleTop_image__QD3l2")
                img = img_element.get_attribute('src')
                print(img)
            except NoSuchElementException:
                print("None")

            driver.close()
            return img

        except NoSuchElementException as e:
            print("Data Not Found")