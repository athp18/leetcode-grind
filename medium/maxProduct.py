class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = res = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr < 0:
                max_product, min_product = min_product, max_product
            max_product = max(curr, max_product*curr)
            min_product = min(curr, min_product*curr) # variable keeping track of minimum we've encountered

            res = max(res, max_product)
        return res
