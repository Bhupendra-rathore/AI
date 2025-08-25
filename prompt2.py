from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
st.header("Research Tool")
paper_input=st.selectbox("Select Research paper name",["Attension Is All you need","BERT: pre-training of Deep Bidirectional Transformers","GPT-3:Language Model are Few-Shot Learners","Diffusion Models Beat GANs on Image Synthesis"])
style_input=st.selectbox("Select Explanation Style",['Beginer-Friendly',"Technical","Code-Oriented","Mathematical"])
length_input=st.selectbox("Select Explanation length",['Short(1-2 paragraphs)',"Medium(3-5 paragraphs)","Long (detailed Explanatuion)"])

template=PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}" with following specifications
Explanation style: {style_input}
Explanation length:{length_input}
""",
input_variables=['papaer_input','style_input','length_input']

)
prompt = template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':style_input
})
if st.button("Summrize"):
    result=model.invoke(prompt)
    st.write(result.content)