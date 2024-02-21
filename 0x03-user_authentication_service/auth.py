#!/usr/bin/env python3
"""
This module defines a hash function that
returns a hash value for a given string.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """
    Generates a random salt and
    hashes the password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            _hash_password(password)
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """Validate login
        """
        dB = DB()
        try:
            usr = dB.find_user_by(email=email)
            if usr:
                bcrypt.checkpw(password.encode('utf-8'), usr.hashed_password)
                return True
        except Exception as e:
            return False
