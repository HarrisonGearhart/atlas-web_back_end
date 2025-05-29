#!/usr/bin/env python3
"""
class is the template for all authentication system
"""

import os
from flask import request
from typing import List, Type, TypeVar


class Auth:
    """
    api authentications
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        does it require authentication
        """
        if path is None:
            return True

        if not excluded_paths or excluded_paths is None:
            return True

        # add a / to the end if it doesnt already
        if not path.endswith('/'):
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        returns header request
        """
        if request is None:
            return None

        if 'Authorization' not in request.headers:
            return None

        # get the authorization
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns current user
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        """
        if request is None:
            return None

        # use get and env
        session_name = os.getenv('SESSION_NAME')

        if session_name is None:
            return None

        # return the value of the cookie
        return request.cookies.get(session_name)
