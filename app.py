from flask import Flask
from auth.routes import auth_bp
from user.routes import user_bp
from admin.routes import admin_bp

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)
