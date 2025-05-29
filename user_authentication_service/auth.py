#!/usr/bin/env python3
"""auth.py"""

import uuid
from typing import Optional
import bcrypt
from sqlalchemy.exc import NoResultFound
from db import DB
from user import User


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user with the database with a hashed password.
        """
        try:  # If this raises a NoResultFound error, user doesn't exist yet
            self._db.find_user_by(email=email)
            #  If above line doesn't raise NoResultFound, user already exists
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            #  User doesn't already exist, proceed with creating user
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if the user login is valid
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode("utf-8"),
                                  user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        Creates a new session with the given email and returns
        the new session_id, or None if the user does not exist
        """
        try:
            user = self._db.find_user_by(email=email)
            new_session_id = _generate_uuid()
            user.session_id = new_session_id
            return new_session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """
        Gets a user from the given session_id
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """
        Destroys a user from the given session_id
        """
        try:
            user = self._db.find_user_by(id=user_id)
            user.session_id = None
        except Exception:
            pass

        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a reset password token
        """
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            user.reset_token = token
            return token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Updates the password for the user with the given reset_token
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            new_hashed_password = _hash_password(password)
            user.hashed_password = new_hashed_password
            user.reset_token = None
            return None
        except Exception:
            raise ValueError


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the hashed password in bytes
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generates a random UUID
    """
    return str(uuid.uuid4())
