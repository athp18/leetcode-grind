# basically, a tree is a connected graph with no cycles
# so, we can just check the definition
# this is a pretty inefficient approach (two depth first searches!) but i will look at it later
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Initialize the graph
        if not n:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def is_connected(n, graph):
            def dfs(node, visited):
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        dfs(neighbor, visited)
            
            visited = set()
            dfs(0, visited)
            return len(visited) == n

        def no_cycle(n, graph):
            def dfs(node, visited, parent):
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        if dfs(neighbor, visited, node):
                            return True
                    elif neighbor != parent:
                        return True
                return False

            visited = [False] * n
            for node in range(n):
                if not visited[node]:
                    if dfs(node, visited, -1):
                        return False
            return True

        return is_connected(n, graph) and no_cycle(n, graph)
