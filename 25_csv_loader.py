from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='HR_Analytics(1).csv')

data=loader.load()

print(data[1])