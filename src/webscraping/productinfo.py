from dataclasses import dataclass
from typing import Optional

#dataclass는 python 3.7 이상부터 사용가능하다. 
#데이터를 저장/전송하는데 사용된다. __init__, __repr__, __eq__ 등의 특수 메서드를 자동으로 생성해준다.
@dataclass
class ProductInfo:
    product_id: int
    site: str
    product_link: Optional[str] = None
    product_img: Optional[str] = None
    original_price: Optional[int] = None
    sales_price: Optional[int] = None
    discount_rate: Optional[int] = None
