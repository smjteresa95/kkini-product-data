from selenium import webdriver

from selenium.webdriver.common.by import By

user_agent_value = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
options = webdriver.FirefoxOptions()
options.add_argument(f"user-agent={user_agent_value}")

search_url = "https://www.coupang.com/np/search?component=&q="
product_to_search = "굿프랜즈 푸짐한한끼왕교자"
url = search_url + product_to_search

driver = webdriver.Firefox(options=options)
driver.get(url)

#쿠키저장
cookies = driver.get_cookies()

#상품명
name_elements = driver.find_elements(By.CLASS_NAME, "name")
name_list = [name_elements[i].text.replace(" ", "") for i in [0, 1, 2, 3, 4]] #요소의 텍스트를 가져오고 공백을 제거한다. 

product_name = product_to_search.replace(" ","")
contains_name = [] #인덱스와 일치하는 상품명 저장할 리스트

for index, s in enumerate(name_list):
    if product_name in s:
        contains_name.append((index, s))

index = contains_name[0][0] 

#상품링크
link_elements = driver.find_elements(By.CLASS_NAME, "search-product-link")
product_link = link_elements[index].get_attribute('href') # 해당 index 요소의 'href'속성값을 가져온다.
print(product_link)

#할인 전 금액
sales_price_elements = driver.find_elements(By.CLASS_NAME, "base-price")
sales_price = sales_price_elements[index].text.replace(",","")
print(sales_price)

#할인 후 금액
sales_price_elements = driver.find_elements(By.CLASS_NAME, "price-value")
sales_price = sales_price_elements[index].text.replace(",","")
print(sales_price)

#할인률
discount_rate_elements = driver.find_elements(By.CLASS_NAME, "instant-discount-rate")
discount_rate = discount_rate_elements[index].text.replace("%","")
print(discount_rate)

driver.quit()
