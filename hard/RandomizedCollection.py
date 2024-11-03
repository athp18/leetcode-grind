import random
from collections import defaultdict

class RandomizedCollection(object):
    def __init__(self):
        self.collection = []
        self.map = defaultdict(set)
        self.length_of_set = 0
        
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # Add val to the collection
        self.collection.append(val)
        self.length_of_set += 1
        self.map[val].add(self.length_of_set - 1)
        k = self.map[val]
        # Return True if it was not present before, False otherwise
        return len(k) == 1

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.map or not self.map[val]:
            return False
        to_remove = self.map[val].pop()
        last = self.collection[-1]
        
        # Replace the value to remove with the last element
        self.collection[to_remove] = last
        # Update map for the last element
        self.map[last].add(to_remove)
        self.map[last].discard(self.length_of_set - 1)
        
        self.collection.pop()
        self.length_of_set -= 1 
        # Clean up the map if no more instances of val
        if not self.map[val]:
            del self.map[val]
        
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.collection)

# Example usage:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
