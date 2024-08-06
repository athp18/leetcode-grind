class Solution: # linear time, constant space
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n, l, MAX, count = len(s), 0, 1, 0
        for r in range(1, n):
            if s[r] == s[r-1]:
                count += 1
            while count > 1:
                if s[l] == s[l+1]:
                    count -= 1
                l += 1
            MAX = max(MAX, r -l + 1)
        return MAX
