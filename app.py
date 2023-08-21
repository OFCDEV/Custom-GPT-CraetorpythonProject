import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

#App Framework
st.title('🦜️🔗GPT Creator')
promt = st.text_input('Plug in your prompt here')

#llms
llm = OpenAI(temperature=0.3)

#Show the stuff to the screen if there is a promt
if promt:
    response = llm(promt)
    st.write(response)

