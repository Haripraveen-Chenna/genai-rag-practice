from app.core.context_builder import build_context
from app.core.prompts import build_prompt

def answer_query(query: str):
    context = build_context(query)
    prompt = build_prompt(query, context)

    # Mock LLM response for practice
    return {
        "answer": f"Answer based on retrieved context for: {query}",
        "sources": context
    }
