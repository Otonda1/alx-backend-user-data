#!/usr/bin/env python3
"""
Introduces a flask app
"""
from flask import Flask, jsonify, request, make_response, abort, redirect
from auth import Auth
from db import DB
AUTH = Auth()

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def message():
    """Returns a JSON message"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Register a new user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def sessions():
    """verifies credentials
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if AUTH.valid_login(email, password) is False:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        response = make_response(jsonify({"email": email,
                                          "message": "logged in"}))
        response.set_cookie('session_id', session_id)
        return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logs out a user
    """
    session_id = request.cookies.get('session_id')
    usr = AUTH.get_user_from_session_id(session_id)
    if usr:
        user_id = getattr(usr, 'id')
        AUTH.destry_session(user_id)
        return redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
