# Let's start with a brute force solution
# This has O(n) space complexity and O(n!) time complexity --> NOT OPTIMAL
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            current = nums[i]
            remaining = nums[:i] + nums[i+1:]
            for p in self.permute(remaining):
                permutations.append([current] + p)
        return permutations

# So, let's do a backtracking approach
# Basically, the algorithm here involves "going back" when we have an optimal solution
# kinda like a decision tree but better
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 0:
            return [[]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result
