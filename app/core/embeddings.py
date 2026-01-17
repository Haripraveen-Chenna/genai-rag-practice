import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("docs")

def store_embeddings(chunks):
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            ids=[f"chunk-{i}"]
        )
