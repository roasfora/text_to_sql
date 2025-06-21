from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
import os

def load_memory():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("vector_store", embeddings)
