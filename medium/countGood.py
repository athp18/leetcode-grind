from collections import defaultdict

class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        pairs = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            pairs += freq[nums[right]] - 1
            
            while pairs >= k:
                count += len(nums) - right
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
                
        return count
