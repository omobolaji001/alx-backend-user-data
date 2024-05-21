#!/usr/bin/env python3
"""Defines Basic Authentication"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Represents Basic Authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header"""

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        base64 = authorization_header.split(" ")[1]
        return base64
