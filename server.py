from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # frontend'den istek atabilmek için

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "")

    # Basit cevap sistemi (backend mantığı burada)
    if "merhaba" in user_msg.lower():
        bot_reply = "Merhaba! Nasılsın?"
    elif "nasılsın" in user_msg.lower():
        bot_reply = "İyiyim, teşekkür ederim. Sen nasılsın?"
    else:
        bot_reply = f"Bunu anlayamadım: {user_msg}"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
