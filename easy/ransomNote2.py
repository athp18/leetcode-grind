class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(magazine) < len(ransomNote):
            return False
        # construct hashmap
        hashmap_mag = {}
        for val in magazine:
            if val in hashmap_mag:
                hashmap_mag[val] += 1
            else:
                hashmap_mag[val] = 1
        
        for val in ransomNote:
            if val not in hashmap_mag or hashmap_mag[val] == 0:
                return False
            hashmap_mag[val] -= 1
        return True
