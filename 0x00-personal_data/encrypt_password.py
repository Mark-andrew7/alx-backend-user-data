#!/usr/bin/env python3
"""
Implement a hash_password function
"""

import bcrypt

def hash_password(password: str) -> str:
    """Returns a hashed password."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()