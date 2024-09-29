import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #initialize graph
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))
        
        #initialize distances
        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        
        # priority queue for dijkstras
        pq = [(0, k)]
        
        while pq:
            dist, node = heapq.heappop(pq)
            
            if dist > distances[node]:
                continue
            
            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        max_dist = max(distances[1:])
        if max_dist != float('inf'):
            return max_dist
        else:
            return -1
