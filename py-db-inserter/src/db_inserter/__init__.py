"""
This package provides a simple interface for database insertion operations, including
insertion, updating, historical logging, and key management.
"""

from .connection import DatabaseConnection
from .operations import DatabaseOperations
from .history import HistoryManager
from .keys import KeyManager
from .config import Config
from .exceptions import DatabaseError, InsertError, UpdateError

__all__ = [
    "DatabaseConnection",
    "DatabaseOperations",
    "HistoryManager",
    "KeyManager",
    "Config",
    "DatabaseError",
    "InsertError",
    "UpdateError"
]