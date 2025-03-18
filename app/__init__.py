from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "your_secret_key_here"
    # Optionally load additional configuration:
    # app.config.from_object("config")

    from app.routes import main  # Import your routes blueprint
    app.register_blueprint(main)

    from app.bot import bot_bp  # Import your bot blueprint
    app.register_blueprint(bot_bp, url_prefix='/bot')

    return app

# Convenience instance (optional)
app = create_app()
