from pydantic import BaseModel
from typing import List, Dict, Any

class BiasState(BaseModel):
    articles: List[Dict[str, Any]] = []
    cleaned_articles: List[Dict[str, Any]] = []
    embeddings: List[Any] = []
    analysis_results: Dict[str, Any] = {}
    comparison_results: str = ""
    final_report: str = ""
