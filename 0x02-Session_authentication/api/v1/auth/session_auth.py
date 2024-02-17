#!/usr/bin/env python3
"""
introduction of new class

"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class

    This class represents the session-based
    authentication mechanism.
    It is responsible for managing user
    sessions and verifying session tokens.

    """
    pass


if issubclass(SessionAuth, Auth):
    print("SessionAuth is a subclass of Auth")
else:
    print("SessionAuth is not a subclass of Auth")
