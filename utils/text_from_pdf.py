from langchain_community.document_loaders import PyPDFLoader

def extract_text_from_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    texts = ""
    for doc in documents:
        texts += doc.page_content + " "
    return texts
