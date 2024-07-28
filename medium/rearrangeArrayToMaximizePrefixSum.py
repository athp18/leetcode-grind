class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i]
        count = 0
        for num in prefix:
            if num > 0:
                count += 1
        return count
