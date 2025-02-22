from retriever import FAQRetriever

def chat():
    retriever = FAQRetriever()
    print("FAQ Chatbot: Ask me anything! Type 'exit' to quit.")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = retriever.get_best_answer(user_input)
        print(f"\nBot: {response}")

if __name__ == "__main__":
    chat()