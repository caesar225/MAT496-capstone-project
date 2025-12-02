def ingest_articles(state):
    cleaned = []
    for article in state.articles:
        content = (
            article["content"]
            .replace("\n", " ")
            .strip()
        )
        cleaned.append({"source": article["source"], "content": content})
    state.cleaned_articles = cleaned
    return state

node_ingest = ingest_articles
