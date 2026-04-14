from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    response = get_response(user_msg)
    return jsonify({"reply": response})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)