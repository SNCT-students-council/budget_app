ROLE_ALLOWED_CATEGORIES = {
    "circle": ["circle"],                 # 同好会は同好会のみ
    "club": ["circle", "project", "club"],# 部活・プロジェクトは全部
    "admin": ["circle", "project", "club"]# 学生会は全部
}

def allowed_categories(role: str):
    return ROLE_ALLOWED_CATEGORIES.get(role, [])
