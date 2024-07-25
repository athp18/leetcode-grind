class Solution(object):
    def generate(self, numRows): # dp solution
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows: # edge case: numRows doesn't exist?
            return [[]]
        dp = [[0] * (i + 1) for i in range(numRows)] # create an empty dp array, initialized with zeroes
        for i in range(numRows): # the first element of each array and the ith element of the ith array are set at 0
            dp[i][0] = 1
            dp[i][i] = 1
        for i in range(2, numRows): 
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # here's the dp part: we just "add" the [i-1][j-1] and [i-1][j] element
        return dp # return the dp array
