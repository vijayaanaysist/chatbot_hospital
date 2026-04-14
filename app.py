from flask import Flask, render_template, request, jsonify
from chatbot import get_response

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
@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        return "Webhook is running ✅"

    req = request.get_json(silent=True, force=True)
    print("REQUEST RECEIVED:", req)

    return jsonify({
        "fulfillmentText": "Webhook connected successfully 🎉"
    })

# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)