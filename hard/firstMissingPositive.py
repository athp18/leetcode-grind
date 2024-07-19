class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                correct = nums[i]-1
                nums[i], nums[correct] = nums[correct], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

    
