# fuck this problem
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (x, y), val in zip(equations, values):
            graph[x][y] = val
            graph[y][x] = 1 / val
        def dfs(x, y, seen):
            if x not in graph or y not in graph:
                return -1.0
            if x == y:
                return 1.0
            seen.add(x)
            for neighbor in graph[x]:
                if neighbor not in seen:
                    res = dfs(neighbor, y, seen)
                    if res != -1.0:
                        return res * graph[x][neighbor]
            seen.remove(x)
            return -1.0
        res = []

        for query in queries:
            seen = set()
            res.append(dfs(query[0], query[1], seen))
        return res
