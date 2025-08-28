from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field


load_dotenv()


model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class Person(BaseModel):

    name:str=Field(description='name of the person')
    age:int=Field(gt=18,description='Age of the person')
    city:str=Field(description='name of the city person belongs to')


parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(
    template='Generate the name,age and city of the fictional {place} person \n {formate_instruction}',
    input_variables=['place'],
    partial_variables={'formate_instruction':parser.get_format_instructions()}

)

# prompt=template.invoke({'place':'Indian'})

# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

chain=template |model|parser

final_result=chain.invoke({'place':'Indian'})

print(final_result)