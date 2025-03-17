from flask import Blueprint, request

bot_bp = Blueprint("bot", __name__)

@bot_bp.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data.get("confidence", 0) > 0.85:
        return "Trade executed", 200
    return "Signal ignored", 200
