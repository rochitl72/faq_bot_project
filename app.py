from flask import Flask, request, jsonify
from retrieve_answer import retrieve_answer

app = Flask(__name__)

@app.route("/ask", methods=["GET"])
def ask():
    query = request.args.get("query", "")
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    answer = retrieve_answer(query)
    return jsonify({"question": query, "answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
