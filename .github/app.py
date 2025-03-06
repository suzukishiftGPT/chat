from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge base for Autocom Japan
knowledge_base = {
    "what is autocom japan": "Autocom Japan is a leading exporter of used cars from Japan.",
    "where is autocom japan located": "Autocom Japan is headquartered in Yokohama, Japan.",
    "what services does autocom japan offer": "Autocom Japan provides car exporting, auction services, and vehicle inspections."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").lower()
    response = knowledge_base.get(user_message, "I'm not sure about that. Ask me about Autocom Japan!")
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
