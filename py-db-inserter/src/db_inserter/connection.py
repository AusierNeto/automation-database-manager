class DatabaseConnection:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        # Logic to establish a database connection
        pass

    def disconnect(self):
        # Logic to close the database connection
        pass

    @property
    def is_connected(self):
        # Logic to check if the connection is active
        return self.connection is not None

    @property
    def connection_parameters(self):
        return {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "database": self.database
        }