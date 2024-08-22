

import urllib3
import json
import pandas as pd
import psycopg2
import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

company_id = '100'
category = 'A01'

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get(
            url='https://www.bigdata-map.kr/api/board/faq?search.page=1&search.rows=10&search.keyword=', 
            headers={
                    'user-agent' : 'Mozilla 5.0', 
                    'Referer':'https://www.bigdata-map.kr/board/faq'
                    }, 
                verify=False)

# 응답이 성공적인지 확인
if response.status_code == 200:
    # JSON 데이터 파싱
    # print(response.text)
    bs = BeautifulSoup(response.text, 'lxml')    
else:
    print(f"Failed to retrieve data: {response.status_code}")

items = json.loads(response.text).get('list')  
# print(items)

for item in items:
    question = item['title']
    answer   = item['content']
    create_dt = item['uploadTs']
    update_dt = item['updateTs']
    
    # print(company_id, category, question, answer, create_dt, update_dt )
    
    with psycopg2.connect(
        host='192.168.0.49',
        dbname='postgres',
        user='postgres',
        password='1234',
        port=5432,
    ) as conn:
        with conn.cursor() as cur:
              cur.execute(f"""INSERT INTO question ( company_id,
                                        category,
                                        question,
                                        answer,
                                        create_dt,
                                        update_dt ) VALUES ('{company_id}', '{category}', '{question}', '{answer}', '{create_dt}', '{update_dt}')""")


