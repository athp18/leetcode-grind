class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []

        for i in range(len(nums)):
            curr = 0
            for j in range(i, len(nums)):
                curr += nums[j]
                sums.append(curr)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)
