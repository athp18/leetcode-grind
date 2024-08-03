class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # good: no repeating chars
        l, r = 0, 2
        count = 0

        while r < len(s):
            if s[l] != s[l+1] and s[l+1] != s[r] and s[l] != s[r]:
                count += 1
            l += 1
            r += 1
        return count
