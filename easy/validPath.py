class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()

        def dfs(node):
            if node == destination:
                return True
            
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)
