class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, z, MAX, n = 0, 0, 0, len(nums)

        for r in range(n):
            if nums[r] == 0:
                z += 1
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            MAX = max(MAX, r - l + 1)
        return MAX
