class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        count, window = {}, {}
        for char in t:
            count[char] = 1 + count.get(char, 0)
        
        have, need, l = 0, len(count), 0
        res, length = [-1, -1], float('inf')

        for r in range(len(s)):
            # right ptr
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count and window[s[r]] == count[s[r]]:
                have += 1
            
            while have == need:
                # update res
                if (r - l + 1) < length:
                    res = [l, r]
                    length = (r - l + 1)
                # pop from l
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l:r+1] if length != float('inf') else ""
