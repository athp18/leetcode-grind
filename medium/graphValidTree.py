from collections import defaultdict

# pretty simple problem here: a tree is just a graph with no cycles, so we're just checking for cycles
class Solution:
    def graphValidTree(self, n, edges):
        # If there are no edges but more than 1 node, it's not a valid tree
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for u, v in edges: # construct adjacency matrix
            graph[u].append(v)
            graph[v].append(u)
        seen = [False] * n # list to keep track of whether we've seen the node or not

        # recursive dfs function
        # we update seen[node] as True
        # the dfs function returns true if we've seen the values, else returns false
        def dfs(node, parent):
            seen[node] = True
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    if dfs(neighbor, node):
                        return True
                elif neighbor != parent:
                    return True
            return False
        
        if dfs(0, -1): # dfs through each value
            return False
        
        if not all(seen): # all seen is True
            return False
        
        return True # return statement
