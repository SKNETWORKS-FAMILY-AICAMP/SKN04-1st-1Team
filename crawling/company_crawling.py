
import urllib3
import json
import psycopg2
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from setting.config import HOST, DB_NAME, USER, PASSWORD, PORT

company_id = '100' #지도 데이터
category_id = 'A01' #기타

def company_crawling_start():
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
        bs = BeautifulSoup(response.text, 'lxml')    
    else:
        print(f"Failed to retrieve data: {response.status_code}")

    items = json.loads(response.text).get('list')  

    print("컴패니 크롤링을 시작합니다")

    for item in tqdm(items):
        question = item['title']
        answer   = item['content']
        
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
                
    print("컴패니 크롤링을 모두 마쳤습니다.")
    return company_id, category_id, question, answer            
