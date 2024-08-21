import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        pq = [(-1.0, start_node)]
        prob = [0.0] * n
        prob[start_node] = 1.0

        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob

            if node == end_node:
                return curr_prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0
