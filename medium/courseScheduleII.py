from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for d, s in prerequisites:
            adj[s].append(d)
            indegree[d] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        num = 0
        
        while queue:
            node = queue.popleft()
            num += 1
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return num == numCourses
