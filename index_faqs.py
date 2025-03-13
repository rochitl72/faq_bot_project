import chromadb
from load_data import load_faqs

# Initialize ChromaDB client (stores data in the "db/" directory)
client = chromadb.PersistentClient(path="db/")

# Load FAQs
faqs = load_faqs()

# Create a Chroma collection
collection = client.get_or_create_collection(name="faqs")

# Index questions
for i, row in faqs.iterrows():
    collection.add(
        ids=[str(i)],  # Unique ID
        documents=[row["question"]],  # Store questions
        metadatas=[{"answer": row["answer"]}]  # Store corresponding answers
    )

print("✅ FAQs Indexed Successfully!")
