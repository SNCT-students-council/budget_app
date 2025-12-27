from flask import Flask, render_template, request

app = Flask(__name__)

# ====== 予算制度データ ======
CATEGORIES = [
    {
        "id": "circle",
        "name": "同好会",
        "budget": 30000,
        "clubs": [
            {"id": "circle_kanko", "name": "観光研究"},
            {"id": "circle_yosakoi", "name": "よさこい"},
            {"id": "circle_video", "name": "動画"},
            {"id": "circle_softball", "name": "ソフトボール"},
            {"id": "circle_science", "name": "理学"},
            {"id": "circle_kado", "name": "華道"},
            {"id": "circle_biology", "name": "生物"},
        ]
    },
    {
        "id": "project",
        "name": "プロジェクト",
        "budget": 50000,
        "clubs": [
            {"id": "project_robocon", "name": "ロボコン"},
            {"id": "project_procon", "name": "プロコン"},
            {"id": "project_ecocar", "name": "エコカー"},
            {"id": "project_desacon", "name": "デザコン"},
            {"id": "project_gcon", "name": "GCON"},
        ]
    },
    {
        "id": "club",
        "name": "部活動",
        "budget": 100000,
        "clubs": [
            {"id": "club_music", "name": "音楽"},
            {"id": "club_ess", "name": "ESS"},
            {"id": "club_photo", "name": "写真"},
            {"id": "club_art", "name": "美術"},
            {"id": "club_literature", "name": "文芸"},
            {"id": "club_igo", "name": "囲碁将棋"},
            {"id": "club_tea", "name": "茶道"},
            {"id": "club_acoustic", "name": "アコギ"},
            {"id": "club_track", "name": "陸上"},
            {"id": "club_badminton", "name": "バドミントン"},
            {"id": "club_baseball", "name": "硬式野球"},
            {"id": "club_softtennis", "name": "ソフトテニス"},
            {"id": "club_tennis", "name": "硬式テニス"},
            {"id": "club_basketball", "name": "バスケ"},
            {"id": "club_wander", "name": "ワンダーフォーゲル"},
            {"id": "club_judo", "name": "柔道"},
            {"id": "club_kendo", "name": "剣道"},
            {"id": "club_mvolley", "name": "男子バレー"},
            {"id": "club_fvolley", "name": "女子バレー"},
            {"id": "club_kyudo", "name": "弓道"},
            {"id": "club_tabletennis", "name": "卓球"},
            {"id": "club_karate", "name": "空手"},
            {"id": "club_handball", "name": "ハンドボール"},
            {"id": "club_soccer", "name": "サッカー"},
            {"id": "club_swimming", "name": "水泳"},
            {"id": "club_rugby", "name": "ラグビー"},
        ]
    }
]



@app.route("/", methods=["GET", "POST"])
def index():
    category_results = []
    submitted = False

    for category in CATEGORIES:
        values = []
        total = 0

        if request.method == "POST":

            for club in category["clubs"]:
                # フォームから値取得（未入力・マイナス防止）
                value = int(request.form.get(club["id"], 0))
                value = max(0, value)

                values.append({
                    "id": club["id"],
                    "name": club["name"],
                    "value": value
                })

                total += value

            remaining = category["budget"] - total

            category_results.append({
                "name": category["name"],
                "budget": category["budget"],
                "clubs": values,   # ← values → clubs に変更
                "total": total,
                "remaining": remaining,
                "ok": remaining == 0
            })
        else:
            for category in CATEGORIES:
                category_results.append({
                    "name": category["name"],
                    "budget": category["budget"],
                    "clubs": [
                        {
                            "id": club["id"],
                            "name": club["name"],
                            "value": 0
                        }
                        for club in category["clubs"]
                    ],
                    "total": 0,
                    "remaining": category["budget"],
                    "ok": False
                })
        all_ok = all(category["ok"] for category in category_results)
        if request.method == "POST":
            if "submit" in request.form and all_ok:
                submitted = True




    return render_template(
        "index.html",
        categories=category_results,
        all_ok=all_ok,
        submitted=submitted
    )


if __name__ == "__main__":
    app.run(debug=True)
