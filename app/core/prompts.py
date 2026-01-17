def build_prompt(query, context):
    return f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{query}

If not found, say "I don't know".
"""
