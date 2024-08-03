class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        num_distinct = len(set(nums))
        n = len(nums)
        count = 0
        
        window = Counter()
        l = 0
        
        for r in range(n):
            window[nums[r]] += 1
            
            while len(window) == num_distinct:
                window[nums[l]] -= 1
                if window[nums[l]] == 0:
                    del window[nums[l]]
                l += 1
            
            count += l
        
        return count
