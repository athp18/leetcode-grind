class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)

        total, remaining = 0, truckSize

        for num, units in boxTypes:
            to_take = min(num, remaining)
            total += to_take * units
            remaining -= to_take

            if remaining == 0:
                break
        return total
