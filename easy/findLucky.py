class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap, MAX = {}, -1
        for a in arr:
            if a in hashmap:
                hashmap[a] += 1
            else:
                hashmap[a] = 1
            
            if hashmap[a] == a:
                MAX = max(MAX, a)
            elif hashmap[a] > a: # handle case where number is once lucky but no longer
                if MAX == a:
                    MAX = -1 # no longer lucky

        MAX = -1
        for k, v in hashmap.items():
            if k == v:
                MAX = max(MAX, k)
        return MAX
