class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        MAX, pigs = minutesToTest // minutesToDie, 0
        while (MAX + 1) ** pigs < buckets:
            pigs += 1
        return pigs
