class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        # Case 1: Max distance between first house and any different-colored house
        i = len(colors) - 1
        while i >= 0 and colors[i] == colors[0]:
            i -= 1
        dist1 = i  # This is the distance from index 0
        
        # Case 2: Max distance between last house and any different-colored house
        j = 0
        while j < len(colors) and colors[j] == colors[len(colors) - 1]:
            j += 1
        dist2 = len(colors) - 1 - j if j < len(colors) else 0  # This is the distance from index n-1
        
        return max(dist1, dist2)
