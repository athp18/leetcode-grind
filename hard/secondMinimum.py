class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        adj = [[] for _ in range(n + 1)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        dist1 = [float('inf')] * (n + 1)
        dist2 = [float('inf')] * (n + 1)
        freq = [0] * (n + 1)
        min_heap = [(0, 1)]
        dist1[1] = 0
        
        while min_heap:
            timeTaken, node = heapq.heappop(min_heap)
            
            freq[node] += 1
            if freq[node] == 2 and node == n:
                return timeTaken
            if (timeTaken // change) % 2:
                timeTaken = change * (timeTaken // change + 1) + time
            else:
                timeTaken += time
            
            for neighbor in adj[node]:
                if freq[neighbor] == 2:
                    continue
                if dist1[neighbor] > timeTaken:
                    dist2[neighbor] = dist1[neighbor]
                    dist1[neighbor] = timeTaken
                    heapq.heappush(min_heap, (timeTaken, neighbor))
                elif dist2[neighbor] > timeTaken and dist1[neighbor] != timeTaken:
                    dist2[neighbor] = timeTaken
                    heapq.heappush(min_heap, (timeTaken, neighbor))
        
        return 0
