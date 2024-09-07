class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, 2 * n
        while l <= r:
            mid = (l + r) // 2
            needed = mid * (mid + 1) // 2
            
            if needed == n:
                return mid
            elif needed < n:
                l = mid + 1
            else:
                r = mid - 1
        return r
