from sentence_transformers import SentenceTransformer

# Initialize embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

def embed_articles(state):
    """
    Embed all articles and store embeddings in the state.
    """
    contents = [a["content"] for a in state.articles]
    state.embeddings = embedder.encode(contents, convert_to_tensor=False)
    state.cleaned_articles = state.articles  # Placeholder for preprocessing
    return state

node_embed = embed_articles
