class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap, MAX = {}, -1
        for a in arr:
            if a in hashmap:
                hashmap[a] += 1
            else:
                hashmap[a] = 1
        for k, v in hashmap.items():
            if k == v:
                MAX = max(MAX, k)
        return MAX
