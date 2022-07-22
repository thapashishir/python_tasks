import flask

from web_app import app
from auth import authenticate

@app.route("/login", methods=["GET"])
def login_get():
    return flask.render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    flask.session["current_user"] = "test_user"
    return flask.redirect("/")

@app.route("/logout", methods=["GET"])
def logout():
    flask.session["current_user"] = None
    return flask.redirect("/login")

@app.route("/", methods=["GET"])
@authenticate
def dashboard():
    return flask.render_template("dashboard.html")


@app.route("/patients", methods=["GET"])
@authenticate
def list_patients():
    return flask.render_template("patients.html")

@app.route("/appointments", methods=["GET"])
@authenticate
def list_appointments():
    return flask.render_template("appointments.html")