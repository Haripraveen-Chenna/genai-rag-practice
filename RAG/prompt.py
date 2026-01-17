def build_prompt(context, question):
    return f"""
You are a knowledgeable assistant.

Answer strictly using the provided context.
Do not use outside knowledge.
If the answer is missing, say:
"The information is not available in the given context."

Format:
- answer with explanation
- small paragraph format

Context:
{context}

Question:
{question}

Answer:
"""
