import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests

st.header('자동차 기업 FAQ')

st.divider()

st.title('HYUNDAI MOBIS')

## 현대 모비스 이미지 삽입
img_url = "https://blog.kakaocdn.net/dn/cLyq53/btqyWVrhfsx/UDMKYI8tkKXLobR2bl6QK1/img.jpg"
st.image(img_url)

st.write("")
st.write("")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['전체', '용품', '부품', '폐차', '멀티미디어', '기타'])
# Perform query.

# Initialize connection.
conn = st.connection("postgresql", type="sql")
df = conn.query('SELECT * FROM question;', ttl="10m")

with tab1:

    
    # Print results.
    option1 = st.selectbox(
    ' ',
    [row.question for row in df.itertuples()], 
    index=0,
    key="1"
    )

    with st.container(border=10):
        for idx, answer in enumerate(list(dict.fromkeys([row.answer for row in df.itertuples()]))):
            if option1 == [row.question for row in df.itertuples()][idx]:
                st.write(answer.replace('<br>','').strip())

with tab2:
    df_a02 = conn.query("SELECT * FROM question WHERE category_id = 'A02';", ttl="10m")
    option2 = st.selectbox(
        ' ',
        [row.question for row in df_a02.itertuples()], 
        index=0,
        key="2"
    )
    with st.container():
        for idx, answer in enumerate(list(dict.fromkeys([row.answer for row in df_a02.itertuples()]))):
            if option2 == [row.question for row in df_a02.itertuples()][idx]:
                st.write(answer.replace('<br>','').strip())

with tab3:
    df_a02 = conn.query("SELECT * FROM question WHERE category_id = 'A02';", ttl="10m")
    option2 = st.selectbox(
        ' ',
        [row.question for row in df_a02.itertuples()], 
        index=0,
        key="2"
    )
    with st.container():
        for idx, answer in enumerate(list(dict.fromkeys([row.answer for row in df_a02.itertuples()]))):
            if option2 == [row.question for row in df_a02.itertuples()][idx]:
                st.write(answer.replace('<br>','').strip())

with tab4:
    df_a02 = conn.query("SELECT * FROM question WHERE category_id = 'A02';", ttl="10m")
    option2 = st.selectbox(
        ' ',
        [row.question for row in df_a02.itertuples()], 
        index=0,
        key="2"
    )
    with st.container():
        for idx, answer in enumerate(list(dict.fromkeys([row.answer for row in df_a02.itertuples()]))):
            if option2 == [row.question for row in df_a02.itertuples()][idx]:
                st.write(answer.replace('<br>','').strip())

