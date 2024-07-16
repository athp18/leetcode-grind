class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def factorial(a):
            # optimize
            dp = [1] * (a + 1)
            for i in range(2, a + 1):
                dp[i] = dp[i - 1] * i
            return dp[a]
        numbers = list(range(1, n + 1))
        result = []
        k -= 1
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            k %= fact
            result.append(str(numbers[index]))
            numbers.pop(index)
        return ''.join(result)
