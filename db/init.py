# db/init.py
from db.connection import get_db

def init_db(app):
    with app.app_context():
        db = get_db()
        cur = db.cursor()
        # submissionsテーブル
        cur.execute("""
        CREATE TABLE IF NOT EXISTS submissions (
            id SERIAL PRIMARY KEY,
            user_id TEXT,
            role TEXT,
            category_id TEXT,
            club_id TEXT,
            amount INTEGER
        )
        """)
        # budgetsテーブル（上限管理）
        cur.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id SERIAL PRIMARY KEY,
            year INTEGER,
            category TEXT,
            club_id TEXT,
            club_name TEXT,
            amount INTEGER
        )
        """)
        db.commit()
        cur.close()
        db.close()
