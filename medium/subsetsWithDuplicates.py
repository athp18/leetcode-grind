class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result
