from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('Disha_Shah_WebDev_Resume.pdf')

doc=loader.load()

print(doc[0].page_content)