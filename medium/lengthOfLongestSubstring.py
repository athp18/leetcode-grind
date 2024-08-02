class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: # edge case: s is an empty string
            return 0

        start, end = 0, 0 # start pointer, end pointer
        curr = set() # set to keep track 

        MAX = 0 # max length

        while end < len(s): # while loop
            if s[end] not in curr: # if the end pointer isnt in curr
                curr.add(s[end]) # we add s[end] 
                end += 1 # we increment the end pointer by 1 (move to the next element)
                MAX = max(MAX, len(curr)) # we update max
            else: # duplicate found
                while s[end] in curr: # edge case: we have continuous duplicates. so we keep shifting the start pointer as long as there are duplicates
                    curr.remove(s[start])
                    start += 1
                curr.add(s[end]) # now we can safely add the end pointer
                end += 1 # and we increment end by 1 (lol)
        return MAX # return the max length
      # we get O(n) time complexity and O(n) space complexity
            
            
