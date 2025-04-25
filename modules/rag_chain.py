from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI #chatting

def get_qa_chain(vector_store):
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash" ,temperature=0.2) # free model of Gem  ,temp =0 perfectly accurate , but not good
    chain = RetrievalQA.from_chain_type(
        llm = llm,
        retriever = vector_store.as_retriever()
    )
    return chain