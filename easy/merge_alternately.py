class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        if len(word1) == len(word2):
            length = len(word1)
            substrings = []
            for i in range(0, length):
                substrings.append(word1[i])
                substrings.append(word2[i])
        else:
            m = min(len(word1), len(word2))
            z = max(len(word1), len(word2))
            substrings = []
            for i in range(m):
                substrings.append(word1[i])
                substrings.append(word2[i])
            if len(word1) < len(word2):
                word1, word2 = word2, word1
            for k in range(m, z):
                substrings.append(word1[k])
        return ''.join(substrings)
