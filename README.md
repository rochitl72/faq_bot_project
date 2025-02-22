
# FAQ Chatbot

A simple FAQ chatbot that retrieves answers from a predefined dataset.

## Features

- Loads FAQ data from a CSV file.
- Uses TF-IDF & cosine similarity for retrieving answers.
- Provides a Flask API for chatbot responses.

## Installation

1. Clone this repository:


## Features  

✔ Reads FAQs from a CSV file  
✔ Cleans and preprocesses text  
✔ Uses **TF-IDF** and **cosine similarity** for matching queries  
✔ Provides a **Flask API** for chatbot responses  
✔ Supports easy dataset expansion  

---

## 1. Installation & Setup  

### Prerequisites  
Ensure you have **Python 3.7+** installed.  

### Clone the Repository  
```sh
git clone https://github.com/yourusername/faq-chatbot.git
cd faq-chatbot

Install Dependencies

pip install -r requirements.txt


---

2. Running the Chatbot

Option 1: Terminal Chatbot

You can run the chatbot in a command-line interface.

python src/chatbot.py

Example Usage:

FAQ Chatbot: Ask me anything! Type 'exit' to quit.

You: What is the company’s refund policy?
Bot: Our refund policy allows returns within 30 days of purchase.

You: exit
Goodbye!


---

Option 2: Flask API Server

Run the chatbot as a web API:

python app.py

This runs the API at http://127.0.0.1:5000/

Testing the API

Use a browser or Postman to test the API by sending a GET request:

http://127.0.0.1:5000/ask?query=How can I contact support?

Example API Response:

{
  "answer": "You can contact customer support at support@example.com."
}


---

3. Project Structure

faq-chatbot/
│── data/                   # Stores FAQ dataset
│   ├── faq.csv             # CSV file with questions and answers
│── src/                    # Core chatbot logic
│   ├── preprocess.py       # Preprocesses text data
│   ├── retriever.py        # Retrieves answers using TF-IDF
│   ├── chatbot.py          # Command-line chatbot interface
│── app.py                  # Flask API for chatbot
│── requirements.txt        # Dependencies
│── README.md               # Documentation


---

4. How to Add More FAQs

You can add more questions and answers by editing data/faq.csv.

CSV Format

question,answer
"What is the company’s refund policy?","Our refund policy allows returns within 30 days of purchase."
"How can I contact customer support?","You can contact customer support at support@example.com."
"Where are your offices located?","Our offices are located in New York, London, and Tokyo."

After Updating the Dataset

Simply restart the chatbot (python src/chatbot.py) or the API (python app.py) to index the new data.


---

5. How It Works (Technical Overview)

1. Data Preprocessing:

Reads faq.csv and converts text to lowercase.

Removes special characters and unwanted symbols.



2. Answer Retrieval (TF-IDF Matching):

Converts questions into TF-IDF vectors.

Uses cosine similarity to find the best-matching answer.

If similarity is below a threshold, returns a fallback message.



3. Flask API:

Serves a /ask endpoint for queries.

Returns JSON responses with the best-matching answer.





---

6. Dependencies

The required dependencies are listed in requirements.txt. Install them using:

pip install -r requirements.txt

Contents of requirements.txt:

flask
pandas
scikit-learn


---

7. Future Improvements

✅ Integrate OpenAI embeddings for better retrieval.
✅ Add support for multilingual queries (via translation APIs).
✅ Implement RAG (Retrieval-Augmented Generation) for dynamic responses.
✅ Allow document uploads to auto-build an FAQ from manuals.


---

8. Troubleshooting & FAQs

1. Flask API not working?

Ensure Flask is installed:

pip install flask

Restart the API:

python app.py

Check if another process is using port 5000. If so, change the port:

python app.py --port 5001


2. Getting incorrect answers?

Ensure your faq.csv is well-formatted.

Increase dataset size for better retrieval.

Modify similarity threshold in retriever.py to fine-tune accuracy.



---

9. License

This project is open-source under the MIT License. Feel free to modify and improve it!

### **How to Use?**
1. Save this file as **`README.md`** in your project folder.
2. When uploaded to GitHub, it will be automatically formatted for easy reading.
3. Users can follow the step-by-step instructions for installation, usage, and troubleshooting.

---

This is a complete **`README.md`** file. Let me know if you need any modifications! 🚀

