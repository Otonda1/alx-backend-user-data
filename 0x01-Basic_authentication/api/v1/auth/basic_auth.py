#!/usr/bin/env python3
"""
class inherits from Auth
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    class inherits from Auth
    """
    pass

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns base64 part of
        the Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
