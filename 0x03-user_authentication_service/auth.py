#!/usr/bin/env python3
"""
This module defines a hash function that
returns a hash value for a given string.
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """
    Generates a random salt and
    hashes the password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """Generate a random UUID
        """
    return str(uuid.uuid4())


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
        try:
            usr = self._db.find_user_by(email=email)
            if usr:
                pwd = getattr(usr, 'hashed_password')
                return bcrypt.checkpw(password.encode(), pwd)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a new session
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                user.session_id = _generate_uuid()
                return user.session_id
        except NoResultFound:
            return
