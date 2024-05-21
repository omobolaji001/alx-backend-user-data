#!/usr/bin/env python3
""" Defines Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Represents a template for all authentication system
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for a given path

        Args:
          - path (str): The path to check
          - excluded_paths (List[str]): List of paths that
            are excluded from authentication

        Return:
          - bool: True if authentication is required otherwise False
        """
        if path is None:
            return True
        if excluded_paths is None or excluded_paths == []:
            return True

        for _path in excluded_paths:
            if _path.rstrip("/") == path.rstrip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header for a given request

        Args:
          - request (optional): The request object.

        Return:
          - str: The authorization header
        """
        if request is None:
            return None
        if request.authorization is None:
            return None

        return request.authorization

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current authenticated user

        Args:
          - request (optional): The request object representing
            the current HTTP request

        Return:
          - str: The current authenticated user
        """
        return None
