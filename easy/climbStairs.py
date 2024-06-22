class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return -1
        if n == 0:
            return 0
        # ok guys let's start with the recursive solution
        #return self.climbStairs(n-1) + self.climbStairs(n-2)
        #but because we're awesome here, lets do dp
        f = [1,1]
        for i in range(2, n+1):
            f.append(f[i-1]+f[i-2])
        return f[n]
        # runtime complexity O(n), space time complexity O(n)
