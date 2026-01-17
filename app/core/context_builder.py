import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("docs")

def build_context(query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results.get("documents", [])
