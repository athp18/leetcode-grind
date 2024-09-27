class Solution: # this is the brute force solution. here, we check each substring equal to the length of p to see if it is an anagram. this is bad
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def isAnagram(a, b):
            if len(a) != len(b):
                return False
            return sorted(a) == sorted(b)
        
        if len(p) > len(s):
            return []
        
        m = len(p)
        res = []
        
        for l in range(len(s) - m + 1):
            if isAnagram(s[l:l+m], p):
                res.append(l)
        
        return res

  class Solution1: # better solution
  
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        
        char_p, char_s = {}, {}
        for i in range(len(p)):
            char_p[p[i]] = 1 + char_p.get(p[i], 0)
            char_s[s[i]] = 1 + char_s.get(s[i], 0)

        res = [0] if char_p == char_s else []
        l = 0
        for r in range(len(p), len(s)):
            char_s[s[r]] = 1 + char_s.get(s[r], 0)
            char_s[s[l]] -= 1

            if char_s[s[l]] == 0:
                char_s.pop(s[l])

            l += 1
            if char_s == char_p:
                res.append(l)
        
        return res
