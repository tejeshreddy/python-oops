"""
Values - Strings
Size of the hmap - 10
Functions - add, get, delete
Chaining - Yes
"""

class HashMap:

    def __init__(self):
        self.TOTAL_COUNT = 10
        self.hmap = [None] * self.TOTAL_COUNT
    
    def _get_hash(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)
        return hash_sum % 10
    
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.hmap[key_hash] == None:
            self.hmap[key_hash] = [key_value]
            return True
        else:
            for pair in self.hmap[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.hmap[key_hash].append(key_value)
            return True
    
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.hmap[key_hash] is not None:
            for pair in self.hmap[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self._get_hash(key)
        if self.hmap[key_hash] == None:
            return None
        for i in range(len(self.hmap[key_hash])):
            if self.hmap[key_hash][i][0] == key:
                self.hmap[key_hash].pop(i)
                return True
        return False
    
    def keys(self):
        arr = []
        for i in range(0, len(self.hmap)):
            if self.hmap[i]:
                arr.extend([j[0] for j in self.hmap[i]])
        print(arr)
    
    def print(self):
        for item in self.hmap:
            if item is not None:
                    print(str(item))


h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.print()
h.add('Ming', '293-8866')
h.print()
h.keys()
                
            
    




    
    
        