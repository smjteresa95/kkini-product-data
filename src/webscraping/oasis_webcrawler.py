from ..util.crawling_util import create_driver
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

class Oasis:

    def __init__(self, product_to_search):
        self.product_to_search = product_to_search

    def ssg_webcrawler(self):
        driver = create_driver()

        search_url = "https://www.oasis.co.kr/product/search?keyword="
        url = search_url + self.product_to_search

        driver.get(url)

        

