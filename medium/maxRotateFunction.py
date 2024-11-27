class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        f_0 = 0
        for i in range(len(nums)):
            f_0 += i * nums[i]
        sum_nums = sum(nums)

        MAX = f_0

        for i in range(1, len(nums)):
            f_0 = f_0 - sum_nums + len(nums) * nums[i-1]
            MAX = max(MAX, f_0)
        return MAX
