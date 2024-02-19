#!/usr/bin/env python3
"""Defines SessionAuth class that represents
   a custom session authenticator
"""

from typing import TypeVar
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
    This class represents the session-based authentication mechanism.
    It is responsible for managing user sessions and verifying session tokens.
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a new session for a user
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id) -> str:
        """
        Returns the User ID based on the session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user based on the session ID in the request.

        Args:
            request (Request): The request object containing the session ID.

        Returns:
            User: The current user object.

        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
