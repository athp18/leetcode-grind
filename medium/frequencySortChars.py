class Solution:
    def frequencySort(self, s: str) -> str:
        hashmap = {}
        res = ""
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        shashmap = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        for key, val in shashmap.items():
            res += key * val
        return res
