from langchain_google_genai import ChatGoogleGenerativeAI  
from dotenv import load_dotenv
from typing import TypedDict,Annotated
from pydantic import BaseModel,Field

load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.0-flash')

json_structure={
    "title":"Review",
    "type":"object",
    "properties":{
        "key_themes":{
            "type":"array",
            "items":{
                "type":"string"
            },
            "description":"write down all the key themes discussed in the review in a list"

        },
        "summary":{
            "type":"string",
            "description":"A brief summary of review"
        },
        "sentiment":{
            "type":"string",
            "enum":["pos","neg"],
            "description":"Return sentiment of the review negative or positive"
        }
    },
    "required": ["key_themes", "summary", "sentiment"]
}


structured_model=model.with_structured_output(json_structure)

result=structured_model.invoke("""
The hardware is great, but the software feels bloated.There are too many 
pre-installed apps that i cant remove. Also , the UI looks outdated compare
to other brands.Hoping for software updates to fix this.

                               """)
print(result)