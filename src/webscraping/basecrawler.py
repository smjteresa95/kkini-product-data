#크롤링 부모 클래스
#웹사이트 크롤링 코드가 중복되어 부모 클래스를 만들고, 상속받아 쓰게끔 한다.
class BaseCrawler:

    def __init__(self, product_id, product_to_search):
        self.product_id = product_id
        self.product_to_search = product_to_search.replace(" ", "")


    def get_product_info(self, crawler_class, product_id, product_to_search):
        crawler_instance = crawler_class(product_id, product_to_search)
        product_info = crawler_instance.webcrawler() #각각의 크롤러에 있는 메서드
        product_info_tuple = (
            product_id,
            getattr(product_info, 'product_link', None),
            getattr(product_info, 'site', None),
            getattr(product_info, 'product_img', None),
            getattr(product_info, 'original_price', None),
            getattr(product_info, 'sales_price', None),
            getattr(product_info, 'discount_rate', None)
        ) 
        return product_info_tuple
