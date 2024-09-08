class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        distances = [float('inf')] * n
        distances[src] = 0

        count = 0
        while count < k + 1:
            temp = distances.copy()
            for f, t, p in flights:
                if distances[f] != float('inf'):
                    temp[t] = min(temp[t], distances[f] + p)
            distances = temp
            count += 1
        
        return distances[dst] if distances[dst] != float('inf') else -1
