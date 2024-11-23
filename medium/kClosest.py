class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclidean_dist(point):
            x, y = point[0], point[1]
            return x**2 + y**2
        
        points.sort(key=euclidean_dist)
        return points[:k]
