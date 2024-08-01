class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r, n = 0, k-1, len(nums)
        res = float('inf')

        while r < n:
            res = min(res, nums[r] - nums[l])
            l += 1
            r += 1
        return res
        
