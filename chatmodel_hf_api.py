# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv
# from langchain_core.messages import HumanMessage
# import os

# load_dotenv()
# # print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))
# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )

# model = ChatHuggingFace(llm=llm)

# result= model.invoke([
#     HumanMessage(content="What is the capital of India?")
# ])
# print(result.content)
