class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        
        for i in range(n - 2):
            l, r = i + 1, n - 1
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
                if current_sum < target:
                    # All triplets with right pointer from left+1 to right are valid
                    count += r - l
                    l += 1
                else:
                    r -= 1
        return count
