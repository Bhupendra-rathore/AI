from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=JsonOutputParser()

template=PromptTemplate(
    template='give me the name age and city of the fictional person \n{formate_instructions}',
    input_variables=[],
    partial_variables={'formate_instructions':parser.get_format_instructions()}
)
chain=template | model | parser
result=chain.invoke({})
print(result)