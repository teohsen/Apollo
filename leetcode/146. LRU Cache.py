class LRUCache:
    def __init__(self, capacity):
        self.dict = {}
        self.freeSpace = capacity


    def get(self, key):
        if key not in self.dict:
            return -1

        self.dict[key] = self.dict.pop(key)

        return self.dict[key]


    def put(self, key, value):
        if key in self.dict:
            self.dict.pop(key)
        else:
            if self.freeSpace:
                self.freeSpace -= 1
            else:
                self.dict.pop(next(iter(self.dict)))

        self.dict[key] = value