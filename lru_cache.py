class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        self.left.next, self.right.prev = self.right, self.left
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, next.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)

            del self.cache[lru.key]


