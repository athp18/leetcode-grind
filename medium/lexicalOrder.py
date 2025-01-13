class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        if not n:
            return []
        
        res = []
        def dfs(curr):
            if curr <= n:
                res.append(curr)
            
            for i in range(10):
                num = curr * 10 + i
                if num <= n:
                    dfs(num)
                else:
                    break
        
        for i in range(1, 10):
            if i <= n:
                dfs(i)

        return res
