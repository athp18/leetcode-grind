class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            if s[l].isalpha() and s[r].isalpha():
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l].isalpha():
                l += 1
            elif s[r].isalpha():
                r -= 1
        return ''.join(s)
