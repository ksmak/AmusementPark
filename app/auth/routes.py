from flask_jwt_extended import create_access_token
from flask import request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from app.auth import bp
from app.extensions import db
from .models import User


@bp.route('/register', methods=['POST'])
def register():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    error = None

    if not username:
        error.append("Username is required.")
    elif not password:
        error.append("Password is required.")

    if error:
        return jsonify({
            'result': 'error',
            'errors': error
        }), 401

    try:
        user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'result': 'OK',
            'errors': None
        })
    except IntegrityError:
        error = f"User {username} is already registered."
        return jsonify({
            'result': 'error',
            'errors': error
        }), 401


@bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    error = None

    if not username:
        error.append("Username is required.")
    elif not password:
        error.append("Password is required.")

    if error:
        return jsonify({
            'result': 'error',
            'errors': error
        }), 401

    user = User.query.filter_by(username=username).first()

    if (not user) or (user.username != username) or \
       (not check_password_hash(user.password, password)):
        return jsonify({
            'result': 'error',
            'error': 'Bad username or password'
        }), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)
