echo from flask import Blueprint, request, jsonify > app\bot.py
echo. >> app\bot.py
echo bot_bp = Blueprint("bot", __name__) >> app\bot.py
echo. >> app\bot.py
echo @bot_bp.route("/webhook", methods=["POST"]) >> app\bot.py
echo def webhook(): >> app\bot.py
echo     data = request.get_json() >> app\bot.py
echo     if data and data.get("confidence", 0) ^> 0.85: >> app\bot.py
echo         return jsonify({^"message^": ^"Trade executed^"}), 200 >> app\bot.py
echo     return jsonify({^"message^": ^"Signal ignored^"}), 200 >> app\bot.py
