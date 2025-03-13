from sentence_transformers import SentenceTransformer

# Download the model and save it locally
model = SentenceTransformer("all-MiniLM-L6-v2")
model.save("model/")  # Saves to the "model/" directory

print("✅ Model downloaded and saved successfully!")
