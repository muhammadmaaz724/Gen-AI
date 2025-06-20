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

chat_template = ChatPromptTemplate([
    ('system','you are a helpfull assistant'),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human','{query}')
    ])

chat_history = []

with open("chat_history.txt") as file:
    chat_history.extend(file.readlines())
    
prompt = chat_template.invoke({
    'chat_history':chat_history,
    'query': "how many houses do i have?"
})

res = model.invoke(prompt)

print(res.content)