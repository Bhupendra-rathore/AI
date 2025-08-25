from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema


load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

schema=[
    ResponseSchema(name='name',description='name of the person'),
    ResponseSchema(name='age',description='age of the person'),
    ResponseSchema(name='city',description='city of the person')
]
parser=StructuredOutputParser.from_response_schemas(schema)
template=PromptTemplate(
    template='give me the name age and city of the fictional person \n{formate_instructions}',
    input_variables=[],
    partial_variables={'formate_instructions':parser.get_format_instructions()}
)
chain=template | model | parser
result=chain.invoke({})
print(result)