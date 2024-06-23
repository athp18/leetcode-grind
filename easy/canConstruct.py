class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}
        # Edge cases
        if len(ransomNote) > len(magazine):
            return False
        if not ransomNote or not magazine:
            return False
        # Part 2
        for char in magazine:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        for c in ransomNote:
            if c in hashmap and hashmap[c] > 0:
                hashmap[c] -= 1
            else:
                return False
        return True
        
      
