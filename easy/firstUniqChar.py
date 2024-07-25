class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = {}
        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
        
        for i, c in enumerate(s):
            if dictionary[c] == 1:
                return i
        return -1
