import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        if not mat:
            return []
        hashmap = {}
        for i in range(len(mat)):
            hashmap[i] = sum(mat[i])
        return heapq.nsmallest(k, hashmap, key=hashmap.get)
        
