## Setup
db_config.py file is hidden by gitignore file. Need  to add db_config.py file under src/config directory.
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

## When using API to fetch data
공공데이터 api로 부터 받아온 값을 DB에 저장한다. 
HTTP 요청을 통해 API로부터 데이터를 받아오는데 python 에서는 requests library를 사용해서 API요청을 처리한다. 
```
pip install requests mysql-connector-python
```

## selenium으로 웹 정보를 받고 BeautifulSoup으로 parsing.
웹페이지가 동적으로 데이터를 로드하기 때문에 requests로 웹 정보를 받을 수가 없어 selenium을 사용해야 한다. 
```
pip install beautifulsoup4
```

## user-agent 찾는 법
1. Firefox를 열고, F12 키를 눌러 개발자 도구를 실행합니다.<br>
2. "네트워크" 탭을 선택합니다.<br>
3. 어떠한 웹 페이지 (예: https://www.google.com)에 접속합니다.<br>
4. 개발자 도구의 네트워크 탭에서, 첫 번째 요청 (보통 웹 페이지의 URL과 일치)을 클릭합니다.<br>
5. 오른쪽의 상세 패널에서 "헤더" 탭을 선택합니다.<br>
6. "요청 헤더" 섹션을 찾아보면 User-Agent라는 항목 아래에 현재 사용 중인 User-Agent 문자열을 볼 수 있습니다.
