def retrieve_similar_texts(state):
    retrieved = {}
    for cluster_id, indices in state.clusters.items():
        retrieved[cluster_id] = [
            state.cleaned_articles[i]["content"]
            for i in indices
        ]
    state.retrieved_docs = retrieved
    return state

node_retrieve = retrieve_similar_texts
