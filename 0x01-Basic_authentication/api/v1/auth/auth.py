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
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the authorization header for a given request

        Args:
          - request (optional): The request object.

        Return:
          - str: The authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the current authenticated user

        Args:
          - request (optional): The request object representing
            the current HTTP request

        Return:
          - str: The current authenticated user
        """
        return None