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

company_id = '200'
category_nos = ['803', '804',  '805', '809']

config = ConfigParser()
config.read('./conf.ini', encoding='utf-8')

HOST     = config['DataBase']['host']
DB_NAME  = config['DataBase']['db_name']
USER     = config['DataBase']['user']
PASSWORD = config['DataBase']['password']
PORT     = config['DataBase']['port']

for category_no in category_nos:
    questions_list = []
    answers_list = []

    url = f'https://www.mobis-as.com/faqLoad.do?pageIndex=1&categoryId={category_no}'
    response = requests.get(url, verify=False)
    
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'lxml')
    
        # List comprehension을 사용하여 질문 텍스트 추출
        questions = [question.text.replace("'",'') for question in bs.select('ul.faq-list li button.tit span')]
        answers = [answer.text.replace("'",'') for answer in bs.select('ul.faq-list div.txt')]
        
        questions_list.extend(questions)
        answers_list.extend(answers)

        if category_no == '803':
            category_id = 'A03'
        elif category_no == '804':
            category_id = 'A04'
        elif category_no == '805':
            category_id = 'A05'
        elif category_no == '809':
            category_id = 'A01'
         
        # 질문과 답변을 딕셔너리로 묶기
        for question, answer in zip(questions_list, answers_list):
         
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
        
        # for question, answer in zip(questions_list, answers_list):
        #     with psycopg2.connect(
        #             host='192.168.0.49',
        #             dbname='postgres',
        #             user='postgres',
        #             password='1234',
        #             port=5432,
        #         ) as conn:
        #             with conn.cursor() as cur:
        #                 cur.execute(f"""INSERT INTO question(company_id,
        #                                             category_id,
        #                                             question,
        #                                             answer ) VALUES (
        #                             '{company_id}', 
        #                             '{category_id}', 
        #                             '{question}', 
        #                             '{answer}')""")
