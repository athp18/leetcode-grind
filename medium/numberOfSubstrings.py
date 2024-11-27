class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int: 
        result = 0
        l = 0
        hashmap = {}

        for c in s:
            hashmap[c] = hashmap.get(c, 0) + 1
            while hashmap[c] == k:
                hashmap[s[l]] -= 1
                l += 1
            result += l
        return result
