from langchain.vectorstores import FAISS
from embedding_utils import embadding_model

def create_vector_store(chunks):
    vectordb = FAISS.from_documents(chunks, embadding_model)
    return vectordb