class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(piles, k, h):
            hours = 0
            for pile in piles:
                hours += -(-pile // k) 
            return hours <= h
    
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if canEatAll(piles, mid, h):
                r = mid
            else:
                l = mid + 1
    
        return l
