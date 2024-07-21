class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ = sum(nums)
        if summ < abs(target) or (summ+target)%2 != 0:
            return 0
        
        newtarget = (summ + target) // 2
        dp = [0] * (newtarget+1)
        dp[0] = 1
        for num in nums:
            for j in range(newtarget, num - 1, -1):
                dp[j] += dp[j-num]
        return dp[newtarget]
