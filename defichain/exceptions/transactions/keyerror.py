

class KeyError(Exception):
    def __init__(self, msg):
        super().__init__(f"KeyError: {msg}")
