class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 + 7

        prefix_sum = [0] * (n+1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        stack = []
        product = 0

        for i in range(n+1):
            while stack and (i == n or nums[stack[-1]] > nums[i]):
                min_index = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                subarray_sum = prefix_sum[right] - prefix_sum[left + 1]
                min_product = nums[min_index] * subarray_sum
                product = max(product, min_product)
            stack.append(i)
        
        return product % mod
