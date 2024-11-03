class RandomizedSet(object):

    def __init__(self):
        self.set = []
        self.length_of_set = 0
        self.map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.append(val)
        self.length_of_set += 1
        self.map[val] = self.length_of_set - 1
        return True


    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            return False
        index_to_remove = self.map[val]
        last_element = self.set[-1]
        self.set[index_to_remove] = last_element
        self.map[last_element] = index_to_remove

        self.set.pop()
        self.map.pop(val, None)
        self.length_of_set -= 1

        return True
    def getRandom(self):
        """
        :rtype: int
        """
        import random
        return random.choice(self.set)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
