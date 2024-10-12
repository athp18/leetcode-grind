class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]: # Recursive approach
      # I'm not hesitant to use this since the length of nums is guarantee to be < 20
        res = []
        self.traverse(nums, 0, 1, res)
        return res
    
    def traverse(self, nums, l, r, int, res):
        if l >= len(nums):  # Check if l is out of bounds
            return
        
        # Adjust r to find the end of the range
        while r < len(nums) and nums[r] - nums[r - 1] == 1:
            r += 1
            
        # Build the range string
        if r - l > 1:  # range exists
            res.append(f"{nums[l]}->{nums[r - 1]}")
        else: #there's a single number
            res.append(str(nums[l]))
        
        # recursive call
        self.traverse(nums, r, r + 1, res)
