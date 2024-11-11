class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 2:
            return 0
        
        right = len(height) - 1
        left = max_area = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

        
