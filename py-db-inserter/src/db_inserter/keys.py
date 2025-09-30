class KeyManager:
    def __init__(self, key_length=16):
        self.key_length = key_length

    def generate_key(self):
        import os
        return os.urandom(self.key_length).hex()

    def validate_key(self, key):
        return isinstance(key, str) and len(key) == self.key_length * 2 and all(c in '0123456789abcdef' for c in key)