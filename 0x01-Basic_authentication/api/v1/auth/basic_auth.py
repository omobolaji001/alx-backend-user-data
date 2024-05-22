#!/usr/bin/env python3
"""Defines Basic Authentication"""
from api.v1.auth.auth import Auth
from typing import TypeVar
from models.user import User
import base64


class BasicAuth(Auth):
    """Represents Basic Authentication"""

    def __init__(self):
        """Instantiates BasicAuth"""
        super().__init__()

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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Returns the decoded value of Base64 string"""

        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Returns the user email and password from Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)

        email_pass = decoded_base64_authorization_header.split(":")

        return (*email_pass,)

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """Returns the User instance based on email and password submitted"""
        if (user_email is None or not isinstance(user_email, str)):
            return None
        if (user_pwd is None or not isinstance(user_pwd, str)):
            return None

        try:
            users = User.search({"email": user_email})
            if not users or users == []:
                return None
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
            return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current authenticated user

        Args:
          - request (optional): The request object representing
            the current HTTP request

        Return:
          - str: The current authenticated user
        """
        auth_header = self.authorization_header(request)
        if auth_header:
            token = self.extract_base64_authorization_header(auth_header)
            if token:
                str_token = self.decode_base64_authorization_header(token)
                if str_token:
                    email, password = self.extract_user_credentials(str_token)
                    if email is not None and password is not None:
                        current_user = self.user_object_from_credentials(
                                email, password)

                        return current_user
        return
