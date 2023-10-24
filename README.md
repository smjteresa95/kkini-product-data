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

## When using API to fetch data
공공데이터 api로 부터 받아온 값을 DB에 저장한다. 
HTTP 요청을 통해 API로부터 데이터를 받아오는데 python 에서는 requests library를 사용해서 API요청을 처리한다. 
```
pip install requests mysql-connector-python
```

