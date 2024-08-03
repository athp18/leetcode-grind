class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        l, MAX = 0, 0

        for r in range(len(nums)):
            hashmap[nums[r]] += 1
            while hashmap[nums[r]] > k:
                hashmap[nums[l]] -= 1
                l += 1
            MAX = max(MAX, r - l + 1)
        return MAX
