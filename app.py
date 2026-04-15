from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import os

app = Flask(__name__)

# ---------------- HOME PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")

# ---------------- CHAT API ----------------
@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    response = get_response(user_msg)
    return jsonify({"reply": response})

# ---------------- DIALOGFLOW WEBHOOK ----------------
@app.route("/webhook", methods=["POST"])
def webhook():
    req = request.get_json(silent=True)
    print("REQUEST RECEIVED:", req)

    return jsonify({
        "fulfillmentText": "Webhook connected successfully 🎉"
    })

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)