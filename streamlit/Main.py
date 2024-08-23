import streamlit as st

st.set_page_config(
  page_title="SKN4th_team1",
  page_icon=":car:"
)

st.write('SKN04-1st-1Team')

st.header(':upside_down_face:  짜않!투않!') 

st.divider()

col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

with col1:
    st.subheader('🐖김정훈')
    st.image('https://avatars.githubusercontent.com/u/48326972?v=4', width=125)

with col2:
    st.subheader('🐴고유림')
    st.image('https://avatars.githubusercontent.com/u/148182017?v=4', width=125)
   
with col3:
    st.subheader('🐱김문수')
    st.image('https://avatars.githubusercontent.com/u/110519720?v=4', width=125)

with col4:
    st.subheader('🐂김효은')
    st.image('https://avatars.githubusercontent.com/u/176723645?v=4', width=125)

st.divider()

st.subheader(':pencil2:프로젝트 개요')
st.write('''
         자동차는 비교적 고가품으로 대표적인 내구재로써 경기상황에 민감합니다. \n
         따라서 자동차 등록대수의 추이는 경기상황을 판단하는 지표가 될 수 있어 전국 자동차 등록 현황의 데이터를 모아 그래프에 나타내고 \n
         CARFAQ 시스템은 한번의 클릭으로 지정된 사이트의 FAQ를 검색하고 전국 자동차 등록 현황을 확인하는 서비스입니다.
         ''')

st.divider()

st.subheader(':pencil2: 프로젝트 소개')
st.write('''
         1. 전국 자동차 등록 현황을 통합하여 데이터베이스를 구축하고, 이를 그래프로 추이를 나타냅니다.
         2. HYUNDAI MOBIS 기업 FAQ 시스템을 설계하여 질문을 카테고리별로 관리하고, 답변 제공 기능을 포함합니다.
         ''')

st.divider()

st.subheader(':point_up: 프로젝트 필요성')
st.write(''' 
자동차 등록 현황에 대한 정보는 다양한 기관과 시스템에 분산되어 있어 일관된 정보를 얻는 것이 어렵습니다. \n
이 프로젝트로 자동차 등록 현황에 대하여 한눈에 들어오는 그래프를 제공하고, 카테고리별로 나눈 기업 FAQ로 정보 접근성을 높입니다.
''')

st.divider()
st.subheader(':shamrock: 프로젝트 목표')
st.write('''
         1. 전국 자동차 등록 현황에 대하여 데이터베이스를 구축하고 이를 그래프로 나타내는 것입니다. \n
         2. 기업 FAQ 시스템을 설계하고 카테고리별로 분류된 질문과 답변 제공 기능을 보입니다.
         ''')
st.divider()
st.subheader(':gear: ERD')
st.image("../image/ERD.png")