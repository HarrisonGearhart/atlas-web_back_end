#!/usr/bin/env python3
"""
Flask App
"""

import flask
from flask import Flask, jsonify, request, redirect
from sqlalchemy.exc import NoResultFound

from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    """GET /"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def users():
    """POST /users"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """POST /sessions"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH._db.find_user_by(email=email)
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            response = jsonify({"email": email, "message": "logged in"})
            response.set_cookie("session_id", session_id)
            return response, 200
    except Exception:
        pass

    flask.abort(401)
    return None


@app.route("/sessions", methods=["DELETE"])
def logout():
    """DELETE /sessions"""
    session_id = request.cookies.get("session_id")
    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        AUTH.destroy_session(user.id)
        return redirect("/")
    except Exception:
        flask.abort(403)
        return None


@app.route("/profile", methods=["GET"])
def profile():
    """GET /profile"""
    session_id = request.cookies.get("session_id")

    try:
        user = AUTH._db.find_user_by(session_id=session_id)
        return {"email": user.email}, 200
    except Exception:
        flask.abort(403)
        return None


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token():
    """POST /reset_password"""
    email = request.form.get("email")
    try:
        user = AUTH._db.find_user_by(email=email)
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except Exception:
        flask.abort(403)
        return None


@app.route("/reset_password", methods=["PUT"])
def update_password():
    """PUT /reset_password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    try:
        user = AUTH._db.find_user_by(email=email)
        if reset_token != user.reset_token:
            flask.abort(403)
            return None
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except NoResultFound:
        flask.abort(403)
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
