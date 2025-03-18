echo from flask import Flask > app\__init__.py
echo. >> app\__init__.py
echo def create_app(): >> app\__init__.py
echo     app = Flask(__name__) >> app\__init__.py
echo     app.config["SECRET_KEY"] = "your_secret_key_here" >> app\__init__.py
echo. >> app\__init__.py
echo     from app.routes import main >> app\__init__.py
echo     app.register_blueprint(main) >> app\__init__.py
echo. >> app\__init__.py
echo     from app.bot import bot_bp >> app\__init__.py
echo     app.register_blueprint(bot_bp, url_prefix="/bot") >> app\__init__.py
echo. >> app\__init__.py
echo     return app >> app\__init__.py
echo. >> app\__init__.py
echo app = create_app() >> app\__init__.py
