class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        MAX = 0

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num in count:
            if num+1 in count:
                MAX = max(MAX, count[num]+count[num+1])
        return MAX
