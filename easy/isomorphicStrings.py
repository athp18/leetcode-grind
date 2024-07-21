class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        def mapping(string):
            mapping = {}
            encoded = []
            for i, char in enumerate(string):
                if char not in mapping:
                    mapping[char] = i
                encoded.append(mapping[char])
            return encoded

        return mapping(s) == mapping(t)
