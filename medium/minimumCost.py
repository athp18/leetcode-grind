class Solution:
    def minimumCost(self, start: str, end: str, orig: List[str], trans: List[str], cost: List[int]) -> int:
        graph = [[] for _ in range(26)]
        for o, t, c in zip(orig, trans, cost):
            graph[ord(o) - ord("a")].append((ord(t) - ord("a"), c))

        # Precalculate minimum costs
        mc = [self._dijkstra(i, graph) for i in range(26)]

        total = 0
        for s, e in zip(start, end):
            if s != e:
                c = mc[ord(s) - ord("a")][ord(e) - ord("a")]
                if c == float("inf"):
                    return -1
                total += c
        return total
    def _dijkstra(self, s, graph):
        pq = [(0, s)]
        d = [float("inf")] * 26 

        while pq:
            dist, u = heapq.heappop(pq)
            if d[u] != float("inf"):
                continue

            d[u] = dist
            for v, c in graph[u]:
                new_dist = dist + c
                if d[v] == float("inf"):
                    heapq.heappush(pq, (new_dist, v))
        return d 
