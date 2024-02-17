#!/usr/bin/env python3
"""
introduction of new class
"""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class"""
    pass


if issubclass(SessionAuth, Auth):
    print("SessionAuth is a subclass of Auth")
else:
    print("SessionAuth is not a subclass of Auth")
