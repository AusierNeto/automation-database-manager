class DatabaseError(Exception):
    """Exception raised for errors in the database operations."""
    pass

class InsertError(DatabaseError):
    """Exception raised for errors during insertion operations."""
    pass

class UpdateError(DatabaseError):
    """Exception raised for errors during update operations."""
    pass

class DeleteError(DatabaseError):
    """Exception raised for errors during delete operations."""
    pass

class ConnectionError(DatabaseError):
    """Exception raised for errors in database connection."""
    pass

class ConfigurationError(DatabaseError):
    """Exception raised for errors in configuration settings."""
    pass