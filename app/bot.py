from flask import Blueprint, request, jsonify

bot_bp = Blueprint("bot", __name__)

@bot_bp.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    if data and data.get("confidence", 0) > 0.85:
        return jsonify({"message": "Trade executed"}), 200
    return jsonify({"message": "Signal ignored"}), 200
