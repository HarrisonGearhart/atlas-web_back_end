#!/usr/bin/env python3
"""
encrypt passwords with bcrypt
"""
import bcrypt


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    validate that provided password matches hashed password
    """
    return bcrypt.checkpw(password.encode(), hashed_password)


def hash_password(password: str) -> bytes:
    """ return a hashed password """
    salt = bcrypt.gensalt()
    encoded_pw = password.encode()
    hashed = bcrypt.hashpw(encoded_pw, salt)
    return hashed
