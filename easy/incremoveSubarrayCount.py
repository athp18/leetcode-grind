class Solution: # not the most efficient or elegant solution (it has o(n2) time complexity) but works
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def increases(arr):
            return all(arr[i] < arr[i + 1] for i in range(len(arr) - 1))
        n, count = len(nums), 0

        for i in range(n):
            for j in range(i, n):
                new = nums[:i] + nums[j+1:]
                if increases(new):
                    count += 1
        return count
