from functools import wraps
from flask import redirect, session


def authenticate(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user = session.get("current_user", None)
        # print(request.url)
        if current_user == None:
            return redirect('/login')

        return f(*args, **kwargs)
    return decorated_function