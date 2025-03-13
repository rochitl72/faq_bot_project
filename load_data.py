import pandas as pd

def load_faqs(file_path="data/faqs.csv"):
    """Load and preprocess FAQ data from CSV with error handling."""
    try:
        df = pd.read_csv(file_path, encoding="utf-8", quotechar='"', skipinitialspace=True)
        
        # Ensure correct column names
        if list(df.columns) != ["question", "answer"]:
            raise ValueError("CSV file format is incorrect. Ensure columns are: question, answer")

        # Convert questions and answers to lowercase
        df['question'] = df['question'].astype(str).str.lower().str.strip()
        df['answer'] = df['answer'].astype(str).str.strip()

        return df
    
    except Exception as e:
        print(f"❌ Error loading FAQs: {e}")
        return None

if __name__ == "__main__":
    faqs = load_faqs()
    if faqs is not None:
        print(faqs.head())  # Print first few entries
