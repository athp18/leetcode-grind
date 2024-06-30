# O(n) time complexity, O(1) space complexity
#ik this is a easy but it felt like a medium
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return "" 
        
        # first string is the initial prefix
        prefix = strs[0]
        
        for i in range(1, len(strs)):  
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]  
        
        return prefix

