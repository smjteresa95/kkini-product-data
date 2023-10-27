import json
from src.config.db_config import DATA_PATH

class GetNutriData:

    #Json 파일에서 데이터 가지고 오기
    @staticmethod #인스턴스 속성이나 메서드가 필요없을 때 사용
    def fetch_json_data_from_file():
        with open(DATA_PATH, encoding="utf8") as f:
            json_data = json.load(f)
        return json_data["records"]


    #데이터에 들어있는 문자 제거.
    @staticmethod
    def subtract_g(value):
        #단위g을 삭제
        return value.replace('g','').strip()


    #우리가 지정한 카테고리 값 넣어주기
    @staticmethod
    def set_category(data):
        categories = {
            "즉석섭취식품": [6, 7, 8, 10 ,11, 12, 13, 14, 16, 18, 19, 23],
            "육가공": [17, 20, 21],
            "음료": [9, 15],
            "간식": [1, 2, 3, 4, 5]
        }
        code = int(data["식품대분류코드"])
        for category, codes in categories.items():
            if code in codes:
                return category
