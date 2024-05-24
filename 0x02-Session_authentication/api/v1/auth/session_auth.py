#!/usr/bin/env python3
"""Defines a class to represent the session authentication"""
from api.v1.auth.auth import Auth
from uuid import uuid4


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
        self.user_id_by_session_id[session_id] = user_id

        return session_id
