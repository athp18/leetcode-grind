class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        def countContributions(is_max):
            stack = []
            res = 0

            for i in range(n + 1):
                while stack and (nums[stack[-1]] < nums[i] if is_max else nums[stack[-1]] > nums[i]):
                    j = stack.pop()
                    k = stack[-1] if stack else -1
                    res += nums[j] * (i - j) * (j - k)
                stack.append(i)
            return res
        
        nums.append(float('inf'))  
        max_sum = countContributions(True)
        nums[-1] = float('-inf')
        min_sum = countContributions(False)
        
        return max_sum - min_sum
