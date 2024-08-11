class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      # the algorithm here is a dfs
      # we basically explore all possible combinations such that the length is equal to k
        def dfs(i, start): 
            if len(curr) == k:
                final.append(curr[:])
                return
            if i > n:
                return
            for j in range(start, n + 1):  
                curr.append(j)
                dfs(i + 1, j + 1) 
                curr.pop()
        curr = []
        final = []

        dfs(0, 1)

        return final
