class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort() # sort the array. while we can choose not to sort the array to avoid overhead, we end up having to do a brute force approach
        count = 0 # initialize count at 0
        for i in range(len(nums)-1, 1, -1): # iterate backwards through the array
            l, r = 0, i - 1 # initialize left and right pointer
            while l < r: # condition
                if nums[l] + nums[r] > nums[i]: # check combo (l, r, i). if is valid, add to count and decrement right pointer
                    count += r-l
                    r -= 1
                else:
                    l += 1 # else, push up left pointer
        return count # O(n2) time complexity, O(1) space complexity

  class Solution1(object): # this is the brute force solution
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isValid(a, b, c): # triangle inequality
            return a + b > c and a + c > b and b + c > a
        
        count = 0
        # check each combo
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if isValid(nums[i], nums[j], nums[k]):
                        count += 1
        
        return count

            
      
