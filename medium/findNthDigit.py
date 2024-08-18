class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n

        while l < r:
            mid = (l + r) // 2
            if self.length(mid) < n:
                l = mid + 1
            else:
                r = mid
        
        total = self.length(l)
        dig = total - n
        return int(str(l)[-dig - 1])
    def length(self, n):
        k, curr, start = 0, 1, 1
        while start <= n:
            end = min(n, start * 10 - 1)
            k += (end - start + 1) * curr
            curr += 1
            start *= 10
        return k

        
