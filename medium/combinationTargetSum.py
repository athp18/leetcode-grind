class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, current, total):
            if total == target:
                result.append(current.copy())
                return
            if i >= len(nums) or total > target:
                return 
            current.append(nums[i])
            dfs(i, current, total+nums[i])
            current.pop()
            dfs(i+1, current, total)
        dfs(0, [], 0)
        return result
