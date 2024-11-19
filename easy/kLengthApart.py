class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distance = 0
        first = False

        for i in range(len(nums)):
            if nums[i] == 1:
                if first and distance < k:
                    return False
                first = True
                distance = 0
            else:
                if first:
                    distance += 1
                first = True
        return True
            
