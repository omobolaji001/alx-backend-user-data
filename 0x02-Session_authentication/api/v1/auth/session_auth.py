#!/usr/bin/env python3
"""Defines a class to represent the session authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """Represents Session Authentication"""

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for user_id

        Args:
                user_id (str): The user_id to create a Session for.

        Return:
                str: Session ID, None if failed
        """
        if not isinstance(user_id, str) or user_id is None:
            return None

        session_id = uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id

        return str(session_id)

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns User ID based on a Session ID"""

        if not isinstance(session_id, str) or session_id is None:
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on cookie value"""
        cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(cookie)

        user = User.get(user_id)
        return user
