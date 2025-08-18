from flask import Flask, request, jsonify
from openai import OpenAI
import base64
import os

app = Flask(__name__)

# API anahtarını burada saklıyoruz, kullanıcı göremez
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
    app.run(host="0.0.0.0", port=5000)
