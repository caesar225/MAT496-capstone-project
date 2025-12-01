from langchain_groq import ChatGroq
import os

# Load Groq API key from environment
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not set in .env")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=api_key
)

def analyze_bias(state):
    """
    Analyze bias for all articles using Groq.
    Returns JSON for each cluster (all articles grouped as one cluster here).
    """
    results = {}
    joined = "\n\n".join([a["content"] for a in state.cleaned_articles])
    prompt = f"""
You are an expert media bias analyst.
Analyze the following news coverage and return JSON only:

Content:
{joined}

Extract:
- political leaning
- sentiment
- emotional / framing language
- key omissions
- bias score (0–10)
"""
    response = llm.invoke(prompt)
    results["cluster_0"] = response.content
    state.analysis_results = results
    return state

node_analyze = analyze_bias
