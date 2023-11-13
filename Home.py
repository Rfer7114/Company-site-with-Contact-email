import streamlit as st
import pandas

st.set_page_config(layout="wide")

content = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of 
type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently 
with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

st.header("The Best Company")
st.write(content)
st.subheader("Our Team")

employee = pandas.read_csv('data.csv')


col1, e1, col2, e2, col3 = st.columns([0.8, 0.1, 0.8, 0.1, 0.8])

with col1:
    for index, value in employee[0:4].iterrows():
        st.subheader(f"{value['first name'].title()} {value['last name'].title()}")
        st.write(value['role'])
        st.image('images/' + value['image'])

with col2:
    for index, value in employee[4:8].iterrows():
        st.subheader(f"{value['first name'].title()} {value['last name'].title()}")
        st.write(value['role'])
        st.image('images/' + value['image'])

with col3:
    for index, value in employee[8:12].iterrows():
        st.subheader(f"{value['first name'].title()} {value['last name'].title()}")
        st.write(value['role'])
        st.image('images/' + value['image'])

