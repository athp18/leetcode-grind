class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in range(n)]
        for edge in edges:
            dist[edge[0]][edge[1]] = edge[2]
            dist[edge[1]][edge[0]] = edge[2]
        for i in range(n):
            dist[i][i] = 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        cityCt = n + 1
        city = -1

        for i in range(n):
            count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if count <= cityCt:
                cityCt = count
                city = i
        return city
