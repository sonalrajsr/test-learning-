from sentence_transformers import SentenceTransformer

embadding_model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    return embadding_model.encode(text, convert_to_tensor=True)