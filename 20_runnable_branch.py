from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough,RunnableBranch

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=StrOutputParser()


prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='summarize the following text{text}',
    input_variables=['text']
)

report_gen_chain=RunnableSequence(prompt1,model,parser)

branch_chain=RunnableBranch(
    (lambda x: len(x.split())>300,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()
)

final_chain=RunnableSequence(report_gen_chain,branch_chain)

print(final_chain.invoke({'topic':'russia vs ukrain'}))