from langchain_core.prompts import ChatPromptTemplate
chat_template= ChatPromptTemplate([
("system",'you are a helpful {domain} expert'),
('human','explain is simple term, what is {topic} ')
])
prompt= chat_template.invoke({'domain':'crcket','topic':'LBW'})
print(prompt)