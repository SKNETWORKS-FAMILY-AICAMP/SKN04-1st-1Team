import psycopg2
import requests
import urllib3
from tqdm import tqdm

# cofig파일
from setting.config import HOST, DB_NAME, USER, PASSWORD, PORT

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def car_reg_info_start():
    # URL 및 페이로드 설정
    url = "https://www.index.go.kr/unity/index/IndexTblGraphAjax.do"
    payload = {
        "idxCd": "1257",
        "sttsCd": "125701",
        "chartOrd": "1",
        "sDate": "1966",
        "eDate": "2023"
    }

    # POST 요청 보내기
    response = requests.post(url, data=payload)
    
    # 요청이 성공했는지 확인
    if response.status_code == 200:
        # JSON 형식으로 변환
        data = response.json()

        # 결과를 출력
        result_list = data.get('resultList', [])
        last_increase_cnt = None
        register_cnt = None

        print("car_reg 크롤링을 시작합니다.")

        for idx, item in enumerate(result_list):
            if int(item['descDt']) > 2013: 
                year = item['descDt']
                if idx % 2 == 0:
                    register_cnt = item['nmbrVal']
                else:
                    last_increase_cnt = item['nmbrVal']
                    with psycopg2.connect(
                            host=HOST,
                            dbname=DB_NAME,
                            user=USER,
                            password=PASSWORD,
                            port=PORT,
                        ) as conn:
                            with conn.cursor() as cur:
                                cur.execute(f"""
                                MERGE INTO car_reg_info AS target
                                USING ( SELECT '{year}' as year, {register_cnt} as register_cnt, {last_increase_cnt} as last_increase_cnt) AS source
                                ON target.year = source.year
                                WHEN NOT MATCHED THEN
                                    INSERT (year, register_cnt, last_increase_cnt)
                                    VALUES (source.year, source.register_cnt, source.last_increase_cnt)""")
                                
    print("car_reg 크롤링을 모두 마쳤습니다.")
    return register_cnt, year, last_increase_cnt
