# fuck this problem
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyMat = [[0 for _ in range(n)] for _ in range(n)]
        for u, v in edges:
            adjacencyMat[u][v] = 1
            adjacencyMat[v][u] = 1
        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            for neighbor, connected in enumerate(adjacencyMat[node]):
                if connected and not visited[neighbor]:
                    dfs(neighbor)
    
        for node in range(n):
            if not visited[node]:
                dfs(node)
                count += 1
                
        return count
            
