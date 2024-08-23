import streamlit as st

st.title(':earth_asia: 전국 자동차 등록 현황')

st.divider()

conn = st.connection("postgresql", type="sql")
df = conn.query('SELECT * FROM car_reg_info;', ttl="10m")

st.subheader('등록대수')
st.bar_chart(df, use_container_width=True, x="year", y="register_cnt", x_label='연도', y_label='등록대수(만대)')

st.divider()

st.subheader('전년대비 증가대수(천대)')
st.line_chart(df, x="year", y="last_increase_cnt", x_label='연도', y_label='전년대비 증가대수(천대)')
