class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach, n = 0, len(nums)

        for i in range(n):
            if i > reach:
                return False
            reach = max(reach, i+nums[i])
            if reach >= n -1:
                return True
        return True
