class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [num for num in nums if num != 0]
        return len(set(arr))
