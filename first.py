import streamlit as st
weight = st.number_input(
    label='enter wight(kg):',
    min_value=5,
    max_value=500,
    value=50

)




hight = st.number_input(
    label='enter wight(kg):',
    min_value=5,
    max_value=500,
    value=50,
    step=0.01
    
)
if st.button('calculater'):
    bmi = weight/hight **2
    st.write(f'your bmii is: {bmi}')