class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}