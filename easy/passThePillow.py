class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycle_length = 2 * (n - 1)
        time_left = time % cycle_length

        if time_left < n - 1:
            return time_left + 1
        else:
            return n - (time_left - (n-1))
