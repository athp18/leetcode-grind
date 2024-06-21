class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer_one = 0
        pointer_two = len(numbers) - 1
        while pointer_one < pointer_two:
            sum_pointers = numbers[pointer_one] + numbers[pointer_two]

            if sum_pointers == target:
                return [pointer_one+1, pointer_two+1]
            elif sum_pointers < target:
                pointer_one += 1
            else:
                pointer_two -= 1
        return
