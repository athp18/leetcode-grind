class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        nums = sorted(set(nums))

        res = length
        r = 0

        for l in range(len(nums)):
            while r < len(nums) and r < nums[r] < nums[l] + length:
                r += 1
            window = r -l + 1
            res = min(res, length-window)
        return res
