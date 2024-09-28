class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        
        @lru_cache(None)
        def dp(i1, i2, length):
            if length == 1:
                return s1[i1] == s2[i2]
            
            for i in range(1, length):
                if (dp(i1, i2, i) and dp(i1 + i, i2 + i, length - i)):
                    return True
                if (dp(i1, i2 + length - i, i) and dp(i1 + i, i2, length - i)):
                    return True
            
            return False
        
        return dp(0, 0, n)
