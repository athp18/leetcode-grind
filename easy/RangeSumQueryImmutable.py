class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        summation = 0
        for i in range(left, right + 1):
            summation += self.nums[i]
        return summation

# lol we can't do that
class NumArray1:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1) # prefix sum array of size nums + 1. why? because the first element is 0 and the array is cumulative
        for i in range(len(nums)): # O(n) time complexity
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i] # since prefix sum is behind by 1 index, we can add its previous element by the corresponding element
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left] # right+1 for inclusive 
        # O(1) space complexity


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
