class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n = len(s)

        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            return left + 1, right
        
        start, end = 0, 0
        for i in range(n):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i+1)

            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
            
        
        return s[start:end]
