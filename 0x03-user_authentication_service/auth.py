#!/usr/bin/env python3
"""Defines _hash_password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a password string and returns it in bytes form
    """
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())
