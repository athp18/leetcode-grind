class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newlst = []
        for char in s:
            if char.isalnum():
                newlst.append(char)
        return newlst == newlst[::-1]
      # easy peasy
