#!/usr/bin/env python3
"""Defines _hash_password
"""
import bcrypt
import uuid
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a password string and returns it in bytes form
    """
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a string of new uuid and returns the string
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register new user user if not already exist
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user
        raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user credentials
        """
        try:
            user = self._db.find_user_by(email=email)
            encoded_password = password.encode('utf-8')
            return bcrypt.checkpw(encoded_password, user.hashed_password)
        except Exception:
            return False
