<<<<<<< HEAD
# Kkini Project를 위한 상품 데이터 정보 저장 및 크롤링 
=======
# Kkini Project를 위한 상품 데이터 정보 크롤링 
>>>>>>> 89f83c8029b4375e0d8e398bcb1755cd5b18f595
### 기능설명

1. **product 테이블** [src/product/parse_data.py]     
json 파일에 담겨있는 5만건의 식품 데이터를 parsing 하는 동시에 is_green, nut_score 계산하여 DB에 Bulk insert.   
> 식품데이터가 담긴 json 파일위치는 src/database/data/nutridata.json 에 있다. testdata.json 은 테스트 할 때 쓴 파일.
2. **product_filter테이블** [src/productfilter/save_nutri_filter.py]     
해당 상품이 저칼로리, 저지방, 고단백인지 등에 대한 계산을 하여 DB에 boolean 값으로 저장한다.
3. **product 테이블** [src/product/save_product_image.py]     
이미지 얻어와서 S3에 저장 
4. **product_info 테이블** [src/webscraping/webscraper.py]     
3개의 사이트에서 상품의 가격, 이미지 등을 크롤링해서 가지고 온다. 
> productinfo.py 파일의 ProductInfo dataclass는 DTO 처럼 데이터를 저장/전송하는데 사용한다. 
5. **DB 쿼리문** [src/data/query.py]          

## Setup

**db_config.py** file is hidden by gitignore file. Need  to add db_config.py file under src/config directory.
```
#딕셔너리 형식으로 DB 설정값 저장 
DB_CONFIG = {
    'host': '',
    'user': '',
    'password': '',
    'database': ''
}

#공공데이터 json 파일경로
DATA_PATH = 'src\\database\\data\\nutridata.json'
```

#PyMySQL이 MySQL 8.0 이후의 새로운 인증 방법인 caching_sha2_password를 사용.
```
pip install cryptography
```

**s3_config.py** file is also hidden by gitignore file. 

```
#Naver Cloud
S3_CONFIG = {
    'service_name' : 's3',
    'access_key': '',
    'secret_key': '',
    'region_name': 'kr-standard',
    'endpoint_url': 'https://kr.object.ncloudstorage.com'
}
```

```
#AWS
# S3_CONFIG = {
#     'service_name' : 's3',
#     'access_key' : '',
#     'secret_key' : '',
#     'region_name': 'ap-northeast-2'
# }
```

**selenium library**
```
pip install selenium
```

**Python과 MySQL 연동을 위한 라이브러리**
```
pip install pymysql
```

## When using API to fetch data
공공데이터 api로 부터 받아온 값을 DB에 저장한다. 
HTTP 요청을 통해 API로부터 데이터를 받아오는데 python 에서는 requests library를 사용해서 API요청을 처리한다.(크롤링으로 가지고 온 이미지 url을 다운받기 위해서도 requests 라이브러리를 사용한다.)
```
pip install requests mysql-connector-python
```

## Object storage 
이미지를 S3에 저장하는 작업을 하기에 앞서 AWS SDK for Python 인 boto3 라이브러리를 설치한다
```
python -m pip install boto3
```


## user-agent 찾는 법
1. Firefox를 열고, F12 키를 눌러 개발자 도구를 실행합니다.<br>
2. "네트워크" 탭을 선택합니다.<br>
3. 어떠한 웹 페이지 (예: https://www.google.com)에 접속합니다.<br>
4. 개발자 도구의 네트워크 탭에서, 첫 번째 요청 (보통 웹 페이지의 URL과 일치)을 클릭합니다.<br>
5. 오른쪽의 상세 패널에서 "헤더" 탭을 선택합니다.<br>
6. "요청 헤더" 섹션을 찾아보면 User-Agent라는 항목 아래에 현재 사용 중인 User-Agent 문자열을 볼 수 있습니다.


## redis
NoSQL(비관계형 데이터베이스)의 한 종류로서 key-value 기반의 인메모리 저장소. RDBMS의 요청부하를 줄이기 위해 인메모리 캐시용도로 사용하기 위해 redis 적용하기로 한다. 
python에서 redis를 사용하기 위해 라이브러리를 설치한다.
```
pip install redis 
```
서버에 redis를 설치해서 데이터 조작이 가능하다.  


## is not accessedPylance 에러
Import "boto3" could not be resolved Pylance reportMissingImports

콘솔창에 pip 새 버전이 나왔다고 자꾸 떴다. Ctrl+Shift+P 키를 눌러 "Python: Select Interpreter"를 검색했더니 맞는 버전의 python interpreter 를 선택할 수 있었다. 