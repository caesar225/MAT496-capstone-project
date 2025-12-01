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

def compare_clusters(state):
    """
    Compare clusters (or articles) to produce a cross-source bias summary.
    """
    prompt = f"""
Compare media bias across these article clusters:

{state.analysis_results}

Return a bullet-point comparison summary.
"""
    response = llm.invoke(prompt)
    state.comparison_results = response.content

    # Combine analysis + comparison into final report
    state.final_report = (
        f"# 📰 Bias Analysis Report\n\n"
        f"Analysis:\n{state.analysis_results}\n\n"
        f"Cross-Source Comparison:\n{state.comparison_results}"
    )
    return state

node_compare = compare_clusters
