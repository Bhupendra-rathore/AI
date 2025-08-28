from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()



prompt=PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['toipc']
)

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=StrOutputParser()

chain=RunnableSequence(prompt,model,parser)

print(chain.invoke({'topic':'AI'}))