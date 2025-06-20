from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(
    llm=llm
)

model = ChatHuggingFace(
    llm=llm
)

with open("chat_history.txt") as file:
    chat_history.extend(file.readlines())
    
    
prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query': "where am i from?"
})

res = model.invoke(prompt)

print(res.content)