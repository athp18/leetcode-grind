class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
      # this is basically building a graph, which is fundamental for i.e. a graph problem
      # you treat the list as a directed graph, where each node points to another
      # basically, you iterate through the adjacent pairs 
      # then, you use a hashmap (graph) to construct an adjacency matrix
      # if any node points to only one other node, you know thats the start of the array
      # finally, you initialize a list and iterate through the hashmap, and append the neighboring nodes
        graph = {}
        for u, v in adjacentPairs:
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        start = None
        for num in graph:
            if len(graph[num]) == 1:
                start = num
                break
        
        n = len(adjacentPairs) + 1
        res = [0] * n
        res[0] = start
        res[1] = graph[start][0]

        for i in range(2, n):
            for neighbor in graph[res[i-1]]:
                if neighbor != res[i-2]:
                    res[i] = neighbor
                    break
        return res
