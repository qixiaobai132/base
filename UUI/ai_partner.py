import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    page_title="智能聊天",
    page_icon="🐺",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)


st.title("智能聊天")

system_prompt = "你是一个智能助手，请回答我的问题。"

prompt = st.chat_input("Say something")
if prompt:
    st.chat_message("user").write(prompt)
    print("调用AI大模型提示词",prompt)
    client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    print(response.choices[0].message.content)
    st.chat_message("assistant").write(response.choices[0].message.content)





