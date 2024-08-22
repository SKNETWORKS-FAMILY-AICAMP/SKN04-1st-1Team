

import urllib3
import json
import pandas as pd
import psycopg2
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

company_id = '300' # car365
category = 'A01'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getCategory(category):
    if category == '기타':
        return 'A01'
    elif category == '폐차':
        return 'A02'

url = 'https://www.car365.go.kr/m3/contents/m3etc_faq_car.do'
response = requests.get(url)

# 응답이 성공적인지 확인
if response.status_code == 200:
    # JSON 데이터 파싱
    # print(response.text)
    bs = BeautifulSoup(response.text, 'lxml')    
else:
    print(f"Failed to retrieve data: {response.status_code}")

# print(response.text)

items = bs.select('table tbody tr')
# print(items)

cnt = 1
for item in items:
    if cnt % 2 == 1:
        category_id = getCategory(item.select('td')[1].text.strip())
        question = item.select('td')[2].text.strip()
    else :
        answer = item.select('td')[1].text.strip()

    # print(item.text)
    if cnt % 2 == 0:
        print(category, question, answer)
    
        with psycopg2.connect(
            host='192.168.0.49',
            dbname='postgres',
            user='postgres',
            password='1234',
            port=5432,
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""INSERT INTO question ( company_id,
                                            category_id,
                                            question,
                                            answer ) VALUES ('{company_id}', '{category_id}', '{question}', '{answer}')""")

    cnt += 1
    # print(company_id, category, question, answer, create_dt, update_dt )
