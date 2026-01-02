from flask import Flask
from db.init import init_db
from auth.routes import auth_bp
from user.routes import user_bp
from admin.routes import admin_bp

app = Flask(__name__)
app.secret_key = "secret-key"
app.config["DATABASE"] = "instance/budget.db"

init_db(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
