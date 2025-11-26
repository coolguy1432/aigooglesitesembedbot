from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Load API key from Render environment variables
client = OpenAI(api_key=os.getenv("API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot for a website."},
                {"role": "user", "content": user_message}
            ]
        )

        return jsonify({
            "reply": response.choices[0].message["content"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return "AI Bot Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
