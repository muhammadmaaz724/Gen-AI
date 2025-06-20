import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize model
model = ChatOpenAI(model='gpt-4')

# Set up initial chat history if not already present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content='You are an experienced doctor based in Pakistan, with years of clinical practice in diagnosing and suggesting treatments. Your role is to simulate realistic doctor-patient conversations for educational purposes only. When a user describes symptoms, provide a potential diagnosis along with commonly prescribed medicines in Pakistan, including their generic names and typical dosage. Clearly state that this is a learning simulation and not a substitute for professional medical advice.')
    ]
    st.session_state.messages = []  # for UI rendering (HumanMessage and AIMessage only)

# Title
st.title("👨‍⚕️ Doctor Chatbot (Educational Purpose Only)")

# Display past chat messages
for message in st.session_state.messages:
    with st.chat_message("user" if isinstance(message, HumanMessage) else "assistant"):
        st.markdown(message.content)

# Input box at the bottom
user_input = st.chat_input("Type Here...")
if user_input:
    # Show user message in chat
    user_msg = HumanMessage(content=user_input)
    st.session_state.chat_history.append(user_msg)
    st.session_state.messages.append(user_msg)
    
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get response from GPT
    response = model.invoke(st.session_state.chat_history)
    ai_msg = AIMessage(content=response.content)
    st.session_state.chat_history.append(ai_msg)
    st.session_state.messages.append(ai_msg)

    # Show AI response in chat
    with st.chat_message("assistant"):
        st.markdown(response.content)
