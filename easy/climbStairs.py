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
        # runtime complexity O(n), space complexity O(n)

class Solution:
    def climbStairs(self, n: int) -> int: # slightly more efficient solution: instead of having an array of n elements, we just use temp vars
        # to update
        if n < 0:
            return -1
        if n == 0:
            return 0
        a, b = 1, 1
        for i in range(2,n+1):
            temp = a + b
            b = a
            a = temp
        return a
