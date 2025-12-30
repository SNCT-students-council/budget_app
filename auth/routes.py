from flask import Blueprint, render_template, request, redirect, url_for, session
from data.users import USERS

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")

        user = next(
            (u for u in USERS if u["id"] == user_id and u["password"] == password),
            None
        )

        if user:
            session["user"] = {
                "id": user["id"],
                "name": user["name"],
                "role": user["role"],
            }

            if user["role"] == "admin":
                return redirect(url_for("admin.dashboard"))
            else:            
                return redirect(url_for("user.user"))
            
        else:
            error = "ID またはパスワードが違います"

    return render_template("user_login.html", error=error)

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
