import pandas as pd
import json
import psycopg2
import requests
import itertools
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from tqdm import tqdm
from configparser import ConfigParser
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
    for idx, item in enumerate(result_list):
        if int(item['descDt']) > 2013: 
            year = item['descDt']
            print(f"년도: {item['descDt']}, 항목: {item['valNm']}, 값: {item['nmbrVal']}")
            if idx % 2 == 0:
                register_cnt = item['nmbrVal']
            else:
                last_increase_cnt = item['nmbrVal']
                with psycopg2.connect(
                        host='192.168.0.49',
                        dbname='postgres',
                        user='postgres',
                        password='1234',
                        port=5432,
                    ) as conn:
                        with conn.cursor() as cur:
                            cur.execute(f"""INSERT INTO car_reg_info_1 (year, register_cnt, last_increase_cnt) VALUES ('{year}', '{register_cnt}', '{last_increase_cnt}')""")