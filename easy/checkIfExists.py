class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set() # use a set for O(1) lookup
        for num in arr: 
            if num / 2 in nums or num * 2 in nums:
                return True
            else:
                nums.add(num)
        return False
