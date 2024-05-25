#!/usr/bin/env python3
"""Defines Session Auth view"""
from api.v1.views import app_views
from flask import abort, request, jsonify
from models.user import User
import os


@app_views.route('/auth_session/login/', methods=['POST'],
                 strict_slashes=False)
def auth_login():
    """Handles user login

    Return:
            Dictionary representation of user,  otherwise error message
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or email == "":
        return jsonify({"error": "email is missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password is missing"}), 400

    users = User.search({'email': email})
    if not users or users == []:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if user.is_valid_password(password):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            session_name = os.getenv('SESSION_NAME')
            response.set_cookie(session_name, session_id)

            return response
    return jsonify({"error": "wrong password"}), 401

@app_views.route('/auth_session/logout/', methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """Logs user out of the current session"""
    from api.v1.views import auth
    if auth.destroy_session():
        return jsonify({}), 200
    abort(404)
