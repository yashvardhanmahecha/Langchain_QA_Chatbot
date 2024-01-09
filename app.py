#Q&A chatbot
#https://huggingface.co/spaces/yashvardhanmahecha/Langchain-QA-Chatbot

from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv() #take environment variables from .env

import streamlit as st

import os

##create a function to load OpenAi model and get response

def get_openai_response(question):
    llm=OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo-instruct", temperature=0.5)
    response=llm(question)
    return response

#initialize our streamlit pp

st.set_page_config(page_title="Q&A demo")  
st.header("GPT 3.5 turbo Langchain Application")

input=st.text_input("Input: ", key="input")

response=get_openai_response(input)

submit=st.button("Ask the question")
if submit:
    st.subheader("The Response is ")
    st.write(response)