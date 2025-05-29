#!/usr/bin/env python3
"""
class BasicAuth that inherits from Auth
"""

import base64
from models.user import User
from typing import TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class BasicAuth that inherits from Auth
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        returns the Base64 part of the Authorization
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        # split after the first 6 characters
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            # variable to hold the decoded bytes
            decoded = base64.b64decode(base64_authorization_header)
            # now decode to utf-8 so we can return as a string
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ':' not in decoded_base64_authorization_header:
            return None, None

        # split email, password at the colon
        # says assume only one colon is used
        email, password = decoded_base64_authorization_header.split(':')

        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # search User email for user_email
        users = User.search({'email': user_email})

        # if there are no matching users then return none
        if not users:
            return None
        # iterate through users, and see if password is valid
        # use the valid password method we created
        # if so return user
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        overloads Auth and retrieves the User instance for a request
        """
        # get header auth from request
        auth_header = self.authorization_header(request)
        # get base 64 auth from auth header
        base64_header = self.extract_base64_authorization_header(auth_header)
        # get decoded header from base64
        decoded_header = self.decode_base64_authorization_header(base64_header)
        # get credentials from decoded header
        email, password = self.extract_user_credentials(decoded_header)
        # now we can retrieve the user
        user = self.user_object_from_credentials(email, password)
        # return the user
        return user
