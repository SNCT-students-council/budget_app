from functools import wraps
from flask import session, redirect, url_for,abort

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("auth.login"))
        return func(*args, **kwargs)
    return wrapper

def role_required(*roles):
    def decorator(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if "user" not in session:
                return redirect(url_for("auth.login"))

            if session["user"]["role"] not in roles:
                abort(403)

            return view(*args, **kwargs)
        return wrapped
    return decorator