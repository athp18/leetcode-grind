# for the 3rd time since i saw this exact question on nd

# brute force dfs
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            positive = dfs(index + 1, current_sum + nums[index])
            negative = dfs(index + 1, current_sum - nums[index])
            
            return positive + negative
            
        return dfs(0, 0)

# better (dp-based) solution
class Solution1:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(index, total):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in dp:
                return dp[(index, total)]
            dp[(index, total)] = (backtrack(index + 1, total + nums[index]) + 
                                  backtrack(index+1, total-nums[index]))
            return dp[(index, total)]
        return backtrack(0, 0)
