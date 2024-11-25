class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return ''.join(str(i) for i in range(k))
        
        seen = set()
        result = []
        initial = "0" * (n-1)
        
        def dfs(node: str):
            for i in range(k):
                new_combination = node + str(i)
                if new_combination not in seen:
                    seen.add(new_combination)
                    next_node = new_combination[1:]
                    dfs(next_node)
                    result.append(str(i))
    
        dfs(initial)
        str_result = ''.join(result)
        return str_result + initial
