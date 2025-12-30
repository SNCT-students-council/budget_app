# admin/routes.py
from flask import Blueprint, render_template, request, session
from auth.decorators import login_required, role_required
from data.categories import CATEGORIES

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/", methods=["GET", "POST"])
@login_required
@role_required("admin")
def dashboard():
    if request.method == "POST":
        for category in CATEGORIES:
            new_budget = request.form.get(f"budget_{category['id']}")
            if new_budget is not None:
                category["budget"] = int(new_budget)

    category_results = []
    grand_total = 0

    for category in CATEGORIES:
        total = sum(club.get("value", 0) for club in category["clubs"])
        remaining = category["budget"] - total

        category_results.append({
            "id": category["id"],
            "name": category["name"],
            "budget": category["budget"],
            "total": total,
            "remaining": remaining
        })

        grand_total += total

    return render_template(
        "admin.html",
        categories=category_results,
        grand_total=grand_total
    )
