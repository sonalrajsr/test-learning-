from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_docs(documents, chunk_size=200, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    return text_splitter.split_text(documents)