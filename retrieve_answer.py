import chromadb
from sentence_transformers import SentenceTransformer

# Load the same model used during indexing
model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_answer(query):
    """Retrieve the best FAQ answer using similarity search."""
    client = chromadb.PersistentClient(path="db/")  # Load ChromaDB
    collection = client.get_or_create_collection(name="faqs")  # Retrieve the collection

    # Convert the query to a vector embedding
    query_vector = model.encode(query.lower().strip()).tolist()

    # Search for the best match using the vector
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=1  # Retrieve the best match
    )

    if results["documents"]:
        return results["metadatas"][0][0]["answer"]  # Get answer from metadata
    else:
        return "❌ Sorry, I couldn't find an answer to that."

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit' to quit): ")
        if query.lower() == "exit":
            break
        answer = retrieve_answer(query)
        print("Bot:", answer)
