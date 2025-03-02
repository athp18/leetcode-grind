class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        def is_missing(index):
            return nums[index] - nums[0] - index

        if k > is_missing(n - 1):
            return nums[n - 1] + k - is_missing(n - 1)
        
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if is_missing(mid) < k:
                left = mid + 1
            else:
                right = mid
        return nums[left - 1] + k - is_missing(left - 1)
