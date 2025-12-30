# user/routes.py
from flask import Blueprint, render_template, request, session
from auth.decorators import login_required, role_required
from data.categories import CATEGORIES
from permissions.rules import allowed_categories

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET", "POST"])
@login_required
@role_required("club", "circle", "admin")

def user():
    role = session["user"]["role"]
    allowed = allowed_categories(role)

    category_results = []
    submitted = False

    for category in CATEGORIES:
        if category["id"] not in allowed:
            continue

        values = []
        total = 0

        if request.method == "POST":
            for club in category["clubs"]:
                value = int(request.form.get(club["id"], 0))
                value = max(0, value)

                values.append({
                    "id": club["id"],
                    "name": club["name"],
                    "value": value
                })
                total += value
        else:
            for club in category["clubs"]:
                values.append({
                    "id": club["id"],
                    "name": club["name"],
                    "value": 0
                })

        remaining = category["budget"] - total

        category_results.append({
            "id": category["id"],
            "name": category["name"],
            "budget": category["budget"],
            "clubs": values,
            "total": total,
            "remaining": remaining,
            "ok": remaining == 0
        })

    all_ok = all(c["ok"] for c in category_results)

    if request.method == "POST" and "submit" in request.form and all_ok:
        submitted = True

    return render_template(
        "user.html",
        categories=category_results,
        all_ok=all_ok,
        submitted=submitted
    )
