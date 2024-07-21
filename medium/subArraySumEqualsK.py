class Solution(object):
    def subarraySum(self, nums, k):
        curr = 0
        total = 0
        freq = {0: 1}
        
        for i in range(len(nums)):
            curr += nums[i]
            target = curr - k
            if target in freq:
                total += freq[target]
            freq[curr] = freq.get(curr, 0) + 1
        
        return total
