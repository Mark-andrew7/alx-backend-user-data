#!/usr/bin/env python3
"""
auth module
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user
        """
        user = self._db.find_user_by(email=email)
        if user:
            raise ValueError(f"User {email} already exists")
        hashed_password = _hash_password(password)
        return self._db.add_user(email, hashed_password)
    
    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user's login
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        
        user_password  = user.hashed_password
        if bcrypt.checkpw(password.encode('utf-8'), user_password):
            return True