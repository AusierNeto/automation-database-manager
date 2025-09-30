class HistoryManager:
    def __init__(self):
        self.history = []

    def log_insert(self, record):
        self.history.append({'action': 'insert', 'record': record})

    def log_update(self, record):
        self.history.append({'action': 'update', 'record': record})

    def get_history(self):
        return self.history
