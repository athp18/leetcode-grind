class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        count = 0
        window = {}
        
        for right in range(n):
            window[nums[right]] = window.get(nums[right], 0) + 1
            
            while max(window) - min(window) > 2:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            
            count += right - left + 1
        
        return count
