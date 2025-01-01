class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [
            (p, (target - p) / s) for p, s in zip(position, speed)
        ]
        
        pairs.sort(reverse=True)
        fleets, prev = 0, 0

        for p, t in pairs:
            if t > prev:
                fleets += 1
                prev = t
        
        return fleets
