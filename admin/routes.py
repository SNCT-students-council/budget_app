from flask import Blueprint, render_template, request, Response
from auth.decorators import login_required, role_required
from db.connection import get_db
from data.categories import CATEGORIES
import io
import csv

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# 学生会ダッシュボード（上限変更）
@admin_bp.route("/", methods=["GET", "POST"])
@login_required
@role_required("admin")
def dashboard():
    db = get_db()

    if request.method == "POST":
        # 上限変更を反映
        for category in CATEGORIES:
            new_budget = request.form.get(f"budget_{category['id']}")
            if new_budget is not None:
                category["budget"] = int(new_budget)
                # budgetsテーブルに反映する場合はここで INSERT/UPDATE
        db.commit()

    # 合計・残金計算
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

# DB確認画面（提出内容）
@admin_bp.route("/db", methods=["GET", "POST"])
@login_required
@role_required("admin")
def admin_db():
    db = get_db()

    # -----------------------------
    # CSV出力
    # -----------------------------
    if request.method == "POST" and "export_csv" in request.form:
        # 全履歴取得（必要に応じて全履歴でも可）
        rows = db.execute("SELECT * FROM submissions ORDER BY id").fetchall()

        output = io.StringIO()
        output.write("\ufeff")  # BOM（Excel用）
        writer = csv.writer(output)
        writer.writerow(["ID", "ユーザーID", "役割", "カテゴリID", "部活ID", "金額"])

        for row in rows:
            writer.writerow([
                row["id"], row["user_id"], row["role"],
                row["category_id"], row["club_id"], row["amount"]
            ])

        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=submissions.csv"}
        )
    
    # -----------------------------
    # 最新提出のみ表示
    # -----------------------------
    # SQLiteで最新IDごとに抽出
    rows = db.execute("""
        SELECT s.*
        FROM submissions s
        INNER JOIN (
            SELECT user_id, category_id, club_id, MAX(id) AS max_id
            FROM submissions
            GROUP BY user_id, category_id, club_id
        ) AS latest
        ON s.user_id = latest.user_id
        AND s.category_id = latest.category_id
        AND s.club_id = latest.club_id
        AND s.id = latest.max_id
        ORDER BY s.id
    """).fetchall()

    return render_template("admin_db.html", rows=rows)
