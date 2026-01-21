from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ALLOWED_KEYWORDS = [
    "fire", "flood", "earthquake", "emergency",
    "injury", "accident", "first aid", "danger"
]

def is_relevant(msg):
    return any(word in msg.lower() for word in ALLOWED_KEYWORDS)

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    if not is_relevant(msg):
        return jsonify({
            "reply": "🚫 I answer only emergency-related questions."
        })

    return jsonify({
        "reply": "⚠️ Stay calm. Move to a safe place and contact emergency services."
    })

if __name__ == "__main__":
    app.run()
