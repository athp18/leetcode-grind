class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = res = nums[0]

        for i in range(1, len(nums)):
            if max_current + nums[i] > nums[i]: # add to subarray
                max_current += nums[i]
            else: 
                # start new subarray
                max_current = nums[i]
            if max_current > res: # update max total
                res = max_current
        return res
