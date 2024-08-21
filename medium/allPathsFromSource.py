class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path, res):
            if node == len(graph) - 1:
                res.append(list(path))
                return
            for n in graph[node]:
                path.append(n)
                dfs(n, path, res)
                path.pop() # backtrack
        res = []
        dfs(0, [0], res)
        return res
