class Solution: # i know this is technically not the most technical solution but im proud of discovering this formula
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        unique, available, curr = 10, 9, 9
        for i in range(2, n +1):
            curr *= available
            unique += curr
            available -= 1
        return unique

