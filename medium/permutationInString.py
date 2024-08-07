class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        need, have = {}, {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        
        l, valid = 0, 0
        for r, c in enumerate(s2):
            if c in need:
                have[c] = have.get(c, 0) + 1
                if have[c] == need[c]:
                    valid += 1
            
            while r - l + 1 >= len(s1):
                if valid == len(need):
                    return True
                lc = s2[l]
                if lc in need:
                    if have[lc] == need[lc]:
                        valid -= 1
                    have[lc] -= 1
                l += 1
                
        return False
