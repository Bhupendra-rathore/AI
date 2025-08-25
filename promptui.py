from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
st.header("Research Tool")
user_input =st.text_input("enter your Prompt")
if st.button("Summrize"):
    result=model.invoke(user_input)
    st.write(result.content)
