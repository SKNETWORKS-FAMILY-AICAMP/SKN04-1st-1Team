import pandas as pd
import json
import requests
import itertools
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from tqdm import tqdm
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'https://www.mobis-as.com/faqLoad.do?pageIndex=1&categoryId=ALL'
response = requests.get(url, verify=False)
if response.status_code == 200:
    questions_list = []

    for page in range(1, 5):
        url = f'https://www.mobis-as.com/faqLoad.do?pageIndex={page}&categoryId=ALL'
        response = requests.get(url, verify=False)
        bs = BeautifulSoup(response.text, 'lxml')
        
        # List comprehension을 사용하여 질문 텍스트 추출
        questions = [question.text for question in bs.select('ul.faq-list li button.tit span')]
        
        # 추출한 질문들을 questions_list에 추가
        questions_list.extend(questions)

questions_list


url = 'https://www.mobis-as.com/faqLoad.do?pageIndex=1&categoryId=ALL'
response = requests.get(url, verify=False)
if response.status_code == 200:
    answers_list = []

    for page in range(1, 5):
        url = f'https://www.mobis-as.com/faqLoad.do?pageIndex={page}&categoryId=ALL'
        response = requests.get(url, verify=False)
        bs = BeautifulSoup(response.text, 'lxml')
        
        # List comprehension을 사용하여 답변 텍스트 추출
        answers = [answer.text for answer in bs.select('ul.faq-list div.txt')]
        
        # 추출한 질문들을 answers_list에 추가
        answers_list.extend(answers)

answers_list