import numpy as np

def cluster_articles(state, threshold=0.75):
    embeddings = np.array(state.embeddings)
    clusters = {}

    # very simple clustering based on cosine similarity
    for i, emb in enumerate(embeddings):
        cluster_id = f"topic-{i}"
        clusters[cluster_id] = [i]

        for j in range(i+1, len(embeddings)):
            sim = np.dot(emb, embeddings[j]) / (np.linalg.norm(emb) * np.linalg.norm(embeddings[j]))
            if sim > threshold:
                clusters[cluster_id].append(j)

    state.clusters = clusters
    return state

node_cluster = cluster_articles
