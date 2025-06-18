from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-4')

st.header("Gen AI Summerizer")

paper_input = st.selectbox("Select Research Paper Name",["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


template = PromptTemplate(
    template="""
    Please summerize the research paper titled "{paper_input}" with the following specifications:
    Explaination style: {style_input}
    Explaination length: {length_input}
    1.Mathematical Details:
        - Include relevent mathematical equations if present in the paper.
        - Explain the mathematical concepts using simple, intuitive code snippets where applicable
        
    2.Analogies:
        - Use relatable analogies to simplify complex ideas.
        if certain information is not available in the paper, respond with "insuficient information available" instead of guessing.
        Ensure the summary is clear, accurate, and aligned with the provided style and length. 
    """,
    input_variables=['paper_input','style_input','length_input']
)

if st.button("Summerize"):
    chain = template | model
    res = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
        }
    )
    
    st.write(res.content)