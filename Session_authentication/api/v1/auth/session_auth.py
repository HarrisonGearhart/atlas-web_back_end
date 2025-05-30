#!/usr/bin/env python3
"""
session auth module
"""

from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """
    inherits from Auth
    """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id
        """
        if user_id is None:
            return None

        if not isinstance(user_id, str):
            return None

        # creating session id
        session_id = str(uuid.uuid4())

        # store the session
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        returns a User ID based on a Session ID
        """
        if session_id is None:
            return None

        if not isinstance(session_id, str):
            return None

        # using get is safer, if there isnt a value
        # then it will return None instead of error
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        (overload) that returns a User instance
        based on a cookie value
        """

        # get session id from cookie
        session_id = self.session_cookie(request)

        user_id = self.user_id_for_session_id(session_id)

        # get from database
        return User.get(user_id)

    def destroy_session(self, request=None) -> bool:
        """
        Deletes the user session (logout)
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        del self.user_id_by_session_id[session_id]
        return True
