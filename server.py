from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# SambaNova / OpenAI tarzı API key
API_KEY = "c49adde8-161b-4412-ac30-55b0b106677d"  # kendi key’inle değiştir
client = OpenAI(api_key=API_KEY, base_url="https://api.sambanova.ai/v1")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "Mesaj boş olamaz."})

    try:
        response = client.chat.completions.create(
            model="Llama-4-Maverick-17B-128E-Instruct",
            messages=[{"role": "user", "content":[{"type":"text","text": user_message}]}],
            temperature=0.7,
            top_p=0.9
        )

        # Yanıt yapısını kontrol et
        if response.choices:
            msg = response.choices[0]
            if hasattr(msg, "message") and msg.message:
                reply = msg.message.content
            elif hasattr(msg, "content"):
                reply = msg.content
            else:
                reply = "Modelden cevap gelmedi."
        else:
            reply = "Modelden cevap gelmedi."

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": f"Hata oluştu: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
