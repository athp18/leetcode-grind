class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        curr_sum = 0
        s = 0

        for e in range(len(nums)):
            curr_sum += nums[e]
            curr_length = e - s + 1

            while curr_sum >= target:
                min_length = min(min_length, curr_length)
                curr_sum -= nums[s]
                s += 1
                curr_length = e - s + 1

        return min_length if min_length != float('inf') else 0
