#!/usr/bin/env python3
"""
This module defines a hash function that
returns a hash value for a given string.
"""
import bcrypt


def _hash_password(password: str) -> str:
    """
    Generates a random salt and
    hashes the password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
