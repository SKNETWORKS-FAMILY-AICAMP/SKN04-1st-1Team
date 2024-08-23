

import urllib3
import psycopg2
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

# cofig파일
from setting.config import HOST, DB_NAME, USER, PASSWORD, PORT

company_id = '300' # car365 
category = 'A01' # 기타

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getCategory(category):
    if category == '기타':
        return 'A01'
    elif category == '폐차':
        return 'A02'

def car365_crawling_start():
    url = 'https://www.car365.go.kr/m3/contents/m3etc_faq_car.do'
    response = requests.get(url)

    # 응답이 성공적인지 확인
    if response.status_code == 200:
        # JSON 데이터 파싱
        bs = BeautifulSoup(response.text, 'lxml')    
    else:
        print(f"Failed to retrieve data: {response.status_code}")

    items = bs.select('table tbody tr')

    print("car365 크롤링을 시작합니다.")

    cnt = 1
    for item in tqdm(items):
        if cnt % 2 == 1:
            category_id = getCategory(item.select('td')[1].text.strip())
            question = item.select('td')[2].text.strip()
        else :
            answer = item.select('td')[1].text.strip()

        if cnt % 2 == 0:
            with psycopg2.connect(
                host=HOST,
                dbname=DB_NAME,
                user=USER,
                password=PASSWORD,
                port=PORT,
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute(f"""
                    MERGE INTO question AS target
                    USING ( SELECT '{company_id}' as company_id, '{category_id}' as category_id, '{question}' as question, '{answer}' as answer ) AS source
                    ON target.question = source.question
                    WHEN NOT MATCHED THEN
                        INSERT (company_id, category_id, question, answer)
                        VALUES (source.company_id, source.category_id, source.question, source.answer)""")           

        cnt += 1
        
    print("car365 크롤링을 모두 마쳤습니다.")
    return company_id, category, question, answer