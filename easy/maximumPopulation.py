class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101
        for b, d in logs:
            years[b-1950] += 1
            years[d-1950] -= 1
        MAX, curr, earliest = 0, 0, 1950

        for y in range(101):
            curr += years[y]
            if curr > MAX:
                MAX = curr
                earliest = 1950 + y
        return earliest
