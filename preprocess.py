import pandas as pd
import re

def load_faq_data(file_path="data/faq.csv"):
    df = pd.read_csv(file_path)
    df['question'] = df['question'].str.lower().apply(lambda x: re.sub(r"[^a-zA-Z0-9\s]", "", x))
    return df

if __name__ == "__main__":
    faq_data = load_faq_data()
    print(faq_data.head())  # Check the cleaned data