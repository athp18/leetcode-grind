class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k - 1
        curr = sum(nums[:k])
        MAX = curr

        while r < len(nums)-1:
            curr = curr - nums[l] + nums[r+1]
            MAX = max(MAX, curr)
            l += 1
            r += 1
        return MAX / k
