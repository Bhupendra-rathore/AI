# to get joke and explanation both others will just give the last proccessed data like only explanation but we want joke as well.

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough

load_dotenv()



prompt1=PromptTemplate(
    template='Generate a joke about  {topic}',
    input_variables=['toipc']
)


prompt2=PromptTemplate(
    template='explain the following joke  {topic}',
    input_variables=['toipc']
)
model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel(
    {'joke':RunnablePassthrough(),
     'explanation':RunnableSequence(prompt2,model,parser)
     }
)

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'Cricket'}))