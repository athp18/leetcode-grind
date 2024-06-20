class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for index, value in enumerate(numbers):
            diff = target - value
            if diff in prevMap:
                return [prevMap[diff], index+1]
            prevMap[value] = index+1
        return
