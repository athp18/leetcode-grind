class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            res = curr = 0
            for num in nums:
                if num <= bound:
                    curr += 1
                else:
                    curr = 0
                res += curr
            return res
        
        return count(right) - count(left - 1)
