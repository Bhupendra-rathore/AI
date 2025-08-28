from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.text_splitter import Language


text="""
def abd():
    print("xyz")
def abc(a):
    print("abc")

a=abc(2)
print(a)
"""


splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=30,
    chunk_overlap=0


)

chunks=splitter.split_text(text)

print(len(chunks))

print(chunks)