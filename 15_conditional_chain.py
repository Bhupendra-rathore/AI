from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from  typing import Literal

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment:Literal['positive','negative']

parser2=PydanticOutputParser(pydantic_object=Feedback)
prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback} \n{formate_instruction}',
    input_variables=['feedback'],
    partial_variables={'formate_instruction':parser2.get_format_instructions()}
)

classifier_chain=prompt1|model |parser2

prompt2=PromptTemplate(
    template='write appropiate statement for this positive feedback \n{feedback}',
    input_variables=['feedback'],
)

prompt3=PromptTemplate(
    template='write appropiate statement for this negative feedback \n{feedback}',
    input_variables=['feedback'],
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment=='positive',prompt2 | model | parser),
    (lambda x:x.sentiment=='negative',prompt3 | model | parser),
RunnableLambda(lambda x: "could not find sentiment")

)

chain=classifier_chain| branch_chain
print(chain.invoke({'feedback':"This is a very good phone"}))


# chain.get_graph().print_ascii()