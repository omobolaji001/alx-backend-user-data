#!/usr/bin/env python3
"""Defines a class to add an expiry date to a Session ID
"""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """Represents a Session Auth with an expiry date"""

    def __init__(self):
        """Instantiates SessionExpAuth"""
        try:
            duration = int(os.getenv('SESSION_DURATION'))
        except Exception:
            duration = 0

        self.session_duration = duration

    def create_session(self, user_id=None):
        """Creates a Session for a user"""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None
        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }
        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Returns User ID for the Session ID provided"""
        if session_id is None:
            return None

        user_data = self.user_id_by_session_id.get(session_id)
        if user_data is None:
            return None

        if self.session_duration <= 0:
            return user_data.get("user_id")

        if "created_at" not in user_data.keys():
            return None

        created_at = user_data.get("created_at")
        allowed_window = created_at + timedelta(seconds=self.session_duration)
        if allowed_window < datetime.now():
            return None

        return user_data.get("user_id")
