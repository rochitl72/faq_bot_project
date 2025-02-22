import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.embeddings.openai import 
OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import pandas as pd

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Load FAQ data
def load_faq_data():
 data = [
        {"Question": "What is our refund policy?", "Answer": "Refunds are processed within 7 days."},
        {"Question": "How do I reset my password?", "Answer": "Go to 
settings and click 'Forgot Password'."}
    ]
    return pd.DataFrame(data)

faq_data = load_faq_data()

# Convert FAQ data to text format
docs = [f"Q: {row['Question']}\nA: 
{row['Answer']}" for _, row in 
faq_data.iterrows()]
vector_db = Chroma.from_documents(docs, 
OpenAIEmbeddings(openai_api_key=openai_api_key))
retriever = vector_db.as_retriever()
qa_chain = 
RetrievalQA.from_chain_type(llm=OpenAI(temperature=0, 
api_key=openai_api_key), retriever=retriever)

# Initialize FastAPI
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/faq")
def faq_query(request: QueryRequest):
    answer = qa_chain.run(request.query)
    return {"answer": answer}

