class Solution: # blind 75 done
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return None
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        for i in range(len(text1) -1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                #condition one: characters in both strings match
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                #condition two: chars dont match
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return dp[0][0]
        
        
