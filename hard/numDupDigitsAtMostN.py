class Solution:
    def numDupDigitsAtMostN(self, n):
        def permute(m, n):
            return 1 if n == 0 else permute(m, n - 1) * (m - n + 1)
        
        n_str = str(n)
        k = len(n_str)
        
        distinct = 0
        for i in range(1, k):
            distinct += 9 * permute(9, i - 1)
        
        seen = set()
        for i in range(k):
            if i == 0:
                start = 1
            else:
                start = 0
            c = int(n_str[i])
            for j in range(start, c):
                if j not in seen:
                    distinct += permute(9 - i, k - i - 1)
            if c in seen:
                break
            seen.add(c)
        else:
            distinct += 1  # n itself
        
        return n - distinct
