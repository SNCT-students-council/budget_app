import sqlite3
import os

def init_db(app):
    os.makedirs("instance", exist_ok=True)

    db_path = app.config["DATABASE"]
    conn = sqlite3.connect(db_path)

    # 予算テーブル
    conn.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            category TEXT,
            club_id TEXT,
            club_name TEXT,
            amount INTEGER
        )
    """)

    # 提出データテーブル
    conn.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            role TEXT,
            category_id INTEGER,
            club_id TEXT,
            amount INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
