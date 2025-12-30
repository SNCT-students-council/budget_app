# data/users.py

"""
ログイン用ユーザーデータ
クラブ代表・学生会を含む
（パスワードは学生会管理前提）
"""

USERS = [
    # ===== 学生会 =====
    {"id": "admin_kaityo"    ,"password": "admin"   ,"name": "学生会","role": "admin"},
    {"id": "admin_kaikeityo" ,"password": "admin"   ,"name": "学生会","role": "admin"},
    

    # ===== 同好会 =====
    {"id": "circle_kanko"    , "password": "circle" , "name": "観光研究", "role": "circle","club_id": "kanko"},
    {"id": "circle_yosakoi"  , "password": "circle" , "name": "よさこい", "role": "circle","club_id": "yosakoi"},
    {"id": "circle_video"    , "password": "circle" , "name": "動画", "role": "circle","club_id": "video"},
    {"id": "circle_softball" , "password": "circle" , "name": "ソフトボール", "role": "circle","club_id": "softball"},
    {"id": "circle_science"  , "password": "circle" , "name": "理学", "role": "circle","club_id": "science"},
    {"id": "circle_kado"     , "password": "circle" , "name": "華道", "role": "circle","club_id": "kado"},
    {"id": "circle_biology"  , "password": "circle" , "name": "生物", "role": "circle","club_id": "biology"},

    # ===== プロジェクト =====
    {"id": "project_robocon" , "password": "project", "name": "ロボコン", "role": "club","club_id": "robocon"},
    {"id": "project_procon"  , "password": "project", "name": "プロコン", "role": "club","club_id": "procon"},
    {"id": "project_ecocar"  , "password": "project", "name": "エコカー", "role": "club","club_id": "ecocar"},
    {"id": "project_desacon" , "password": "project", "name": "デザコン", "role": "club","club_id": "desacon"},
    {"id": "project_gcon"    , "password": "project", "name": "GCON", "role": "club","club_id": "gcon"},

    # ===== 部活動 =====
    {"id": "club_music"      , "password": "club"   , "name": "音楽", "role": "club","club_id": "music"},
    {"id": "club_ess"        , "password": "club"   , "name": "ESS", "role": "club","club_id": "ess"},
    {"id": "club_photo"      , "password": "club"   , "name": "写真", "role": "club","club_id": "photo"},
    {"id": "club_art"        , "password": "club"   , "name": "美術", "role": "club","club_id": "art"},
    {"id": "club_literature" , "password": "club"   , "name": "文芸", "role": "club","club_id": "literature"},
    {"id": "club_igo"        , "password": "club"   , "name": "囲碁将棋", "role": "club","club_id": "igo"},
    {"id": "club_tea"        , "password": "club"   , "name": "茶道", "role": "club","club_id": "tea"},
    {"id": "club_acoustic"   , "password": "club"   , "name": "アコギ", "role": "club","club_id": "acoustic"},
    {"id": "club_track"      , "password": "club"   , "name": "陸上", "role": "club","club_id": "track"},
    {"id": "club_badminton"  , "password": "club"   , "name": "バドミントン", "role": "club","club_id": "badminton"},
    {"id": "club_baseball"   , "password": "club"   , "name": "硬式野球", "role": "club","club_id": "baseball"},
    {"id": "club_softtennis" , "password": "club"   , "name": "ソフトテニス", "role": "club","club_id": "softtennis"},
    {"id": "club_tennis"     , "password": "club"   , "name": "硬式テニス", "role": "club","club_id": "tennis"},
    {"id": "club_basketball" , "password": "club"   , "name": "バスケ", "role": "club","club_id": "basketball"},
    {"id": "club_wander"     , "password": "club"   , "name": "ワンダーフォーゲル", "role": "club","club_id": "wander"},
    {"id": "club_judo"       , "password": "club"   , "name": "柔道", "role": "club","club_id": "judo"},
    {"id": "club_kendo"      , "password": "club"   , "name": "剣道", "role": "club","club_id": "kendo"},
    {"id": "club_mvolley"    , "password": "club"   , "name": "男子バレー", "role": "club","club_id": "mvolley"},
    {"id": "club_fvolley"    , "password": "club"   , "name": "女子バレー", "role": "club","club_id": "fvolley"},
    {"id": "club_kyudo"      , "password": "club"   , "name": "弓道", "role": "club","club_id": "kyudo"},
    {"id": "club_tabletennis", "password": "club"   , "name": "卓球", "role": "club","club_id": "tabletennis"},
    {"id": "club_karate"     , "password": "club"   , "name": "空手", "role": "club","club_id": "karate"},
    {"id": "club_handball"   , "password": "club"   , "name": "ハンドボール", "role": "club","club_id": "handball"},
    {"id": "club_soccer"     , "password": "club"   , "name": "サッカー", "role": "club","club_id": "soccer"},
    {"id": "club_swimming"   , "password": "club"   , "name": "水泳", "role": "club","club_id": "swimming"},
    {"id": "club_rugby"      , "password": "club"   , "name": "ラグビー", "role": "club","club_id": "rugby"},
]
