import os
from flask import Flask
from .bot import bot_bp
from .auth import auth_bp

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_key")
app.config["API_KEY"] = os.getenv("API_KEY", "default_api_key")
app.config["BROKER_API_URL"] = os.getenv("BROKER_API_URL", "https://api.deriv.com/v2/trade")
app.config["WEBSOCKET_URL"] = os.getenv("WEBSOCKET_URL", "wss://ws.deriv.com/websockets/v3")
app.config["DATABASE_URL"] = os.getenv("DATABASE_URL", "")
app.config["PORT"] = int(os.getenv("PORT", 5000))

app.register_blueprint(bot_bp, url_prefix='/bot')
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route("/")
def hello():
    return "Hello, World!"
