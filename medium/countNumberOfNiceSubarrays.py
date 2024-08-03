class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, l, curr, pref = 0, 0, 0, 0 
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                curr += 1
                pref = 0
            
            while curr == k:
                if nums[l] % 2 != 0:
                    curr -= 1
                l += 1
                pref += 1
            
            count += pref
        
        return count
