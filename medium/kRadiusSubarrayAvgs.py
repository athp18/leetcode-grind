class Solution: # O(n) space complexity and O(n) time complexity
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = [-1] * n

        window = 2 * k + 1 # (i+k) - (i-k) + 1 = 2k + 1, basic math
        if n < window: # theres nothing less than the window
            return res
        curr = sum(nums[:window]) # the current sum
        for i in range(k, n-k):
            res[i] = curr // window # do the actual avg
            if i + k + 1 < n: # bounds check
                curr += nums[i+k+1] - nums[i-k] # we add the element entering and leaving the element respectively to curr
        return res
        
