class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i
        
        start = end = 0
        res = []
        for i in range(len(s)):
            end = max(end, hashmap[s[i]])

            if i == end:
                res.append(end - start + 1)
                start = i + 1
        return res
