#!/usr/bin/env python3

from api.v1.views import app_views
from flask import jsonify, request, abort
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ defins a path for the login route """
    mail = request.form.get('email')
    pwd = request.form.get('password')
    if mail is None or mail == "":
        return jsonify({"error": "email missing"}), 400
    if pwd is None or pwd == "":
        return jsonify({"error": "password missing"}), 400
    users = User.search({'email': mail})
    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(pwd):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        res = jsonify(user.to_json())
        res.set_cookie("session_id", session_id)
        return res
