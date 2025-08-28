from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableLambda,RunnableParallel,RunnablePassthrough

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser=StrOutputParser()

prompt=PromptTemplate(
    template='write a joke about the {topic}',
    input_variables=['topic']
)
def word_counter(text):
    return len(text.split())
    

joke_gen_chain=RunnableSequence(prompt,model,parser)

parallel_chain=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':RunnableLambda(word_counter)
    }
)
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_chain.invoke({'topic':'Virat'}))
