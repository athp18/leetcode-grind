class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        var = float('-inf')
        
        for num in reversed(nums):
            if num < var:
                return True
            while stack and stack[-1] < num:
                var = stack.pop()
            stack.append(num)
        
        return False
