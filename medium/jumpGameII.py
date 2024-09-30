class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = curr = furthest = 0
        for i in range(n - 1):
            furthest = max(furthest, i + nums[i])
            if i == curr:
                jumps += 1
                curr = furthest
                if curr >= n - 1:
                    break
        return jumps
