from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import base64

app = Flask(__name__)
CORS(app)  # Tüm frontend isteklerine izin ver

# API anahtarı güvenli şekilde burada
client = OpenAI(
    api_key="c49adde8-161b-4412-ac30-55b0b106677d",
    base_url="https://api.sambanova.ai/v1",
)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    image_base64 = data.get("image_base64", None)

    messages = [{"role": "user", "content": question}]
    if image_base64:
        messages[0]["content"] += "\n[IMAGE_BASE64:" + image_base64 + "]"

    try:
        response = client.chat.completions.create(
            model="Llama-4-Maverick-17B-128E-Instruct",
            messages=messages,
            temperature=0.1,
            top_p=0.1
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Hata: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
