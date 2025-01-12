class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""
        
        counter = Counter(s)

        heap = [(-count, c) for c, count in counter.items()] # for max heap before, we want max heaps since we wanna pop the most frequent character first
        heapq.heapify(heap)

        res = []
        while len(heap) >= 2:
            top_count, top_c = heapq.heappop(heap)
            next_count, next_char = heapq.heappop(heap)
            res.append(top_c)
            res.append(next_char)

            if top_count + 1:
                heapq.heappush(heap, (top_count+1, top_c))
            if next_count + 1:
                heapq.heappush(heap, (next_count+1, next_char))
            
        if heap:
            top_count, top_c = heapq.heappop(heap)
            if top_count != -1 or (res and top_c == res[-1]):
                return ""
            else:
                res.append(top_c)
        
        return ''.join(res)
