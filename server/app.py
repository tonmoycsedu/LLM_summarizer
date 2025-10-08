from flask import Flask, jsonify, request
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)  # Allow Vue frontend to call the API
    

@app.route("/api/chat", methods=["POST"])
def echo_message():
    data = request.get_json()
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=data
    )
    # print(response.text)
    return jsonify({"message": response.text})

if __name__ == "__main__":
    app.run(debug=True, port=5001)