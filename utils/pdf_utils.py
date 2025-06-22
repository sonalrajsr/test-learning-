from langchain_community.document_loaders import PyPDFLoader
 
def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    text = ""
    for doc in documents:
        text += doc.page_content
    return text

from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(docs, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)
