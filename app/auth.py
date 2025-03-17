from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            return redirect(url_for("hello"))
    return render_template("login.html")
