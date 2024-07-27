class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newlst = []
        for char in s:
            if char.isalnum():
                newlst.append(char)
        return newlst == newlst[::-1]
      # easy peasy
class Solution1: # better, more optimal solution
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
