from src.webscraping.coupang_webcrawler import Coupang
from src.webscraping.ssg_webcrawler import Ssg

Ssg_instance = Ssg("굿프랜즈 푸짐한한끼왕교자")
Ssg_instance.ssg_crawler()

coupang_instance = Coupang("굿프랜즈 푸짐한한끼왕교자")
coupang_instance.coupang_webcrawler()