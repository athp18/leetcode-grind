class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to nodes

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        #left - least recently used, right - most recently used
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev, NEXT = node.prev, node.next
        prev.next, NEXT.prev = NEXT, prev

    def insert(self, node):
        prev, NEXT = self.right.prev, self.right
        prev.next = NEXT.prev = node
        node.next, node.prev = NEXT, prev

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
            # remove from LL and remove from hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
