from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import preprocess

class FAQRetriever:
    def __init__(self):
        self.faq_data = preprocess.load_faq_data()
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.faq_data['question'])

    def get_best_answer(self, query):
        query = query.lower()
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.question_vectors).flatten()
        best_match_idx = similarities.argmax()

        if similarities[best_match_idx] < 0.2:  # Confidence threshold
            return "Sorry, I couldn't find an exact answer. Please contact support."
        
        return self.faq_data.iloc[best_match_idx]['answer']

if __name__ == "__main__":
    retriever = FAQRetriever()
    user_query = input("Ask a question: ")
    print(retriever.get_best_answer(user_query))