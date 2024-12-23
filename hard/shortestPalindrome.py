class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s
        
        for i in range(len(s), -1, -1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                remaining = s[i:]
                return remaining[::-1] + s
        return s
        
