import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(find_dotenv())
llm = ChatOpenAI(model="gpt-4o-mini")
print(llm.invoke("Xin chào?").content)
