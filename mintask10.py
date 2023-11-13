class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = dict()

    def put(self, key, value):
        if key in self.cache:
            self.cache[key][1] += 1
            return
        if len(self.cache) == self.capacity:
            self.cache.pop(self.__find_min())
        self.cache[key] = [value, 1]

    def get(self, key):
        if key in self.cache:
            self.cache[key][1] += 1
            return self.cache[key][0]
        return None

    def __find_min(self):
        return min(self.cache.items(), key=lambda x: x[1][1])[0]
