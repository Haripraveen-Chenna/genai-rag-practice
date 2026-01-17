from evaluation.retrieval_eval import cosine_similarity
from evaluation.answer_quality_eval import extract_keywords
from evaluation.grounding_eval import grounding_score


def evaluate_retrieval(q, retriever, embedder):
    q_emb = embedder.encode([q])[0]
    doc = retriever.retrieve(q, 1)[0]
    d_emb = embedder.encode([doc["text"]])[0]
    return round(float(cosine_similarity(q_emb, d_emb)), 3)


def evaluate_rag(q, retriever, generator, embedder):
    # 🔹 retrieve docs once
    docs = retriever.retrieve(q, 2)
    context = " ".join(d["text"] for d in docs)

    # 🔹 generate answer once
    answer = generator.generate(q, docs)

    # ---- Retrieval score ----
    retrieval_score = evaluate_retrieval(q, retriever, embedder)

    # ---- Answer quality ----
    keywords = extract_keywords(context)
    hits = sum(k in answer.lower() for k in keywords)
    answer_quality = round(hits / max(len(keywords), 1), 3)

    # ---- Grounding ----
    grounding = grounding_score(answer, context)

    return {
        "question": q,
        "answer": answer,
        "retrieval": retrieval_score,
        "answer_quality": answer_quality,
        "grounding": grounding
    }
