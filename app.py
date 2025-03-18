import openai
import os
from flask import Flask, request, jsonify

# ✅ Replace "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" with your actual OpenAI API key
OPENAI_API_KEY = "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"

# ✅ Set up OpenAI client
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

# ✅ Set up Flask app
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"error": "No message provided."}), 400
    
    try:
        response = openai_client.chat.completions.create(  # ✅ Corrected API call
            model="gpt-4",  # Use GPT-4 or GPT-3.5
            messages=[
                {"role": "system", "content": "You are a legal assistant specializing in trust creation. Ask the user structured questions to build a trust."},
                {"role": "user", "content": user_message},
            ]
        )
        
        reply = response.choices[0].message.content  # ✅ Fixed response extraction
        return jsonify({"response": reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)  # Runs locally on http://127.0.0.1:5000