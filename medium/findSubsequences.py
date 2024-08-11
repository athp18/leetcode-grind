class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            if len(path)> 1:
                res.add(tuple(path)) # avoid duplicates
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:
                    backtrack(i + 1, path + [nums[i]])
        res = set()
        backtrack(0, [])
        return list(res)
