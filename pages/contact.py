import streamlit as st
import pandas
import send_email as se


st.set_page_config(layout='wide')
st.header("Contact Us")
with st.form(key="contact_form"):

    user_email = st.text_input(label="Your Email address", placeholder="eg: abc@gmail.com")

    opt = pandas.read_csv('topics.csv')

    opt = st.selectbox(label="What topic do you want to discuss", options=opt)

    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New mail from {user_email} for topic {opt}

From: {user_email}
{raw_message}
"""

    send_button = st.form_submit_button("Send")

    if send_button:
        se.send_email(message)
        st.info("Message sent successfully")



