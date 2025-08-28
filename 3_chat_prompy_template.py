from langchain_core.prompts import ChatPromptTemplate

chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert'),
    ('human','Explain in simple terms , What is {topic}')
   ])

prompt=chat_template.invoke({'domain':'cricket','topic':'LBW'})

print(prompt)