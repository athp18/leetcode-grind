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
