class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        dp = {}
        curr = 0

        for i in range(len(s)):
            follows = ord(s[i]) - ord(s[i-1])
            if i > 0 and follows % 26 == 1:
                curr += 1
            else:
                curr = 1
            
            char = s[i]
            dp[char] = max(dp.get(char, 0), curr)
        return sum(dp.values())
