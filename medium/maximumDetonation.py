class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        
        # Build the graph
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, _ = bombs[j]
                    distance = ((x1-x2)**2 + (y1-y2)**2) ** 0.5
                    if distance <= r1:
                        graph[i].append(j)
        
        def dfs(node, visited):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)
            return len(visited)
        
        max_detonated = 0
        for i in range(n):
            detonated = dfs(i, set())
            max_detonated = max(max_detonated, detonated)
        
        return max_detonated
