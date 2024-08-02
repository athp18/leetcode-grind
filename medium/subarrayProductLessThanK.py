class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:  # edge case where k is less than or equal to 1
            return 0
        
        res = 0
        l, prod = 0, 1
        for r in range(len(nums)):
            prod *= nums[r]
            while prod >= k and l <= r:
                prod //= nums[l] # divide the prod so its *not* greater than k and make sure the l pointer is less than the r pointer
                l += 1
            res += (r - l + 1)
        return res
