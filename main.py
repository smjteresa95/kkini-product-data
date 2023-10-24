from src.nutridata.parse_data import insert_sql_from_json

if __name__ == '__main__':

    #DB에 기준일 이후의 공공데이터 저장 
    insert_sql_from_json('2023-08-09')
    
