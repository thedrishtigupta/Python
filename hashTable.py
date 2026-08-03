
class HashTable:
    def __init__(self):
        self.collection = dict()
    
    def hash(self, string):
        return sum(ord(ch) for ch in string)

    def add(self, key, value):
        hashed = self.hash(key)

        if hashed not in self.collection:
            self.collection[hashed] = {}

        self.collection[hashed][key] = value

    def remove(self, key):
        hashed = self.hash(key)

        if hashed in self.collection and key in self.collection[hashed]:
            del self.collection[hashed][key]

            if not self.collection[hashed]:
                del self.collection[hashed]

    def lookup(self, key):
        hashed = self.hash(key)

        if hashed in self.collection:
            return self.collection[hashed].get(key)

        return None