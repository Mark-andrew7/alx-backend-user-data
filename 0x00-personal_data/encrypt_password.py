#!/usr/bin/env python3
"""
Implement a hash_password function
"""

import bcrypt

def hash_password(password: str) -> str:
    """Returns a hashed password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def is_valid(hashed_password: str, password: str) -> bool:
    """Returns a boolean."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())