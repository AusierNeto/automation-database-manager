class Config:
    def __init__(self, db_name, user, password, host='localhost', port=5432):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def load_from_file(self, config_file):
        import json
        with open(config_file, 'r') as file:
            config = json.load(file)
            self.db_name = config.get('db_name', self.db_name)
            self.user = config.get('user', self.user)
            self.password = config.get('password', self.password)
            self.host = config.get('host', self.host)
            self.port = config.get('port', self.port)