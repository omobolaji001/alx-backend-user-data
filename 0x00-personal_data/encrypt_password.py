#!/usr/bin/env python3
"""Defines a function to encrpyt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password"""
    password_bytes = password.encode()
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password_bytes, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates password"""
    password_bytes = password.encode()

    return bcrypt.checkpw(password_bytes, hashed_password)
