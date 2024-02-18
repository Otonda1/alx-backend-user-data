#!/usr/bin/env python3
"""Defines SessionAuth class that represents
   a custom session authenticator
"""

from api.v1.auth.auth import Auth
from uuid import uuid4


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
