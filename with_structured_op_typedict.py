# wont work with gemini but will work with openai models




# from langchain_google_genai import ChatGoogleGenerativeAI  
# from dotenv import load_dotenv
# from typing import TypedDict,Annotated

# load_dotenv()

# model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')


# class Review(TypedDict):

#     summary:Annotated[str,'a breif summary of review']
#     key_themes:Annotated[list[str],'write down all key points discussed in the review']
#     sentiment:str


# structured_model=model.with_structured_output(Review)

# result=structured_model.invoke("""
# The hardware is great, but the software feels bloated.There are too many 
# pre-installed apps that i cant remove. Also , the UI looks outdated compare
# to other brands.Hoping for software updates to fix this.

#                                """)
# print(result)