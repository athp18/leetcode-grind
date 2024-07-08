class Solution:
    def countSubstrings(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            num += self.countPalindromes(s, i, i)
            num += self.countPalindromes(s, i, i+1)
        return num
    def countPalindromes(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res
