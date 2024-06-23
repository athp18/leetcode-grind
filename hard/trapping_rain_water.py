# Algorithm: min(left[i], right[i]) - heights[i]
# Why does this work? Well, the possible rainwater trapped at index i has to have a height of the minimum of the shorter of the bars next to it
# (else there is overflow). Then, you have to subtract heights[i] because the bar itself takes up some space that you have to account for
# This is an O(n) time complexity solution and O(n) space complexity 
class Solution:
    def trap(self, height: List[int]) -> int:
        def find_max_left(arr):
            max_left = [0] * len(arr)
            max_so_far = float('-inf')
            for i in range(len(arr)):
                max_left[i] = max_so_far
                if arr[i] > max_so_far:
                    max_so_far = arr[i]
            return max_left
        def find_max_right(arr):
            max_right = [0] * len(arr)
            max_so_far = float('-inf')
            for i in range(len(arr) - 1, -1, -1):
                max_right[i] = max_so_far
                if arr[i] > max_so_far:
                    max_so_far = arr[i]
            return max_right
        
        if not height:
            return 0

        left_arr = find_max_left(height)
        right_arr = find_max_right(height)
        
        sums = [0] * len(height)
        for i in range(len(height)):
            k = min(left_arr[i], right_arr[i]) - height[i]
            if k > 0:
                sums[i] = k
            else:
                sums[i] = 0 # can't be negative
        
        return sum(sums)

## O(1) memory solution (two pointers)
class Solution1:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        result = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                result += leftMax - height[l] 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                result += rightMax - height[r]
        return result
      
