class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Base case: return an empty set as the only subset of an empty set
        if not nums:
            return [[]]
        else:
            first_element = nums[0]
            rest = nums[1:]
            subsets = []
            for subset in self.subsets(rest):
                subsets.append(subset)
                subsets.append([first_element] + subset)
            return subsets

## OR:

from copy import deepcopy as copy

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        curr = []
        subsets = []

        def search(i):
            if i == len(nums):
                subsets.append(copy(curr))
                print('Out of bounds error')
                return
            curr.append(nums[i])
            search(i+1)
            curr.pop()
            search(i+1)
        
        search(0)
        return subsets
