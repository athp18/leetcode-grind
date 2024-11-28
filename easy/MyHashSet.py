class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(997)]

    def add(self, key: int) -> None:
        hashkey = key % 997
        if not self.contains(key):
            self.buckets[hashkey].append(key)

    def remove(self, key: int) -> None:
        hashkey = key % 997
        bucket = self.buckets[hashkey]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        hashkey = key % 997
        return key in self.buckets[hashkey]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
