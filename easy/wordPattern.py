class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split()
        if len(pattern) != len(s):
            return False
        a = {}
        b = {}
        for i, j in zip(pattern, s):
            if (i in a and a[i] != j) or (j in b and b[j] != i):
                return False
            a[i] = j
            b[j] = i
        return True
