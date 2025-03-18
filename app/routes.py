echo from flask import Blueprint, render_template > app\routes.py
echo. >> app\routes.py
echo main = Blueprint("main", __name__) >> app\routes.py
echo. >> app\routes.py
echo @main.route("/") >> app\routes.py
echo def home(): >> app\routes.py
echo     return render_template("analysis.html") >> app\routes.py
