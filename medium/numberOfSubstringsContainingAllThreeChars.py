class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {c: 0 for c in 'abc'}
        l, res = 0, 0
        
        for r in range(len(s)):
            count[s[r]] += 1
            
            while all(count.values()):
                count[s[l]] -= 1
                l += 1
            
            res += l
        
        return res
