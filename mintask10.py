class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = dict()

    def put(self, key, value):
        if len(self.cache) == self.capacity:
            first_key = list(self.cache.keys())[0]
            self.cache.pop(first_key)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            self.put(key, self.cache[key])
            return self.cache[key]
        return None


a = LRUCache()
for i in range(1, 20):
    a.put(i, i)

a.get(4)
a.put(100, 100)

print(a.cache)
