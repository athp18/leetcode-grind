class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp_left = [0] * len(nums)
        dp_left[0] = nums[0]
        for i in range(1, len(nums)):
            dp_left[i] = nums[i] + dp_left[i-1]
        dp_right = [0] * len(nums)
        dp_right[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            dp_right[i] = nums[i] + dp_right[i + 1]
        for i in range(len(nums)):
            if dp_right[i] == dp_left[i]:
                return i
        return -1
        # praise god
