class Solution:
    def same(self, s: str) -> bool:
        return len(set(s)) == 1

    def has(self, s: str, n: int) -> bool:
        hashmap = {}
        for i in range(len(s) - n + 1):
            aux = s[i:i+n]
            if self.same(aux):
                hashmap[aux] = hashmap.get(aux, 0) + 1
                if hashmap[aux] >= 3:
                    return True
        return False

    def maximumLength(self, s: str) -> int:
        n = len(s)
        ans = -1
        for i in range(1, n):
            if self.has(s, i):
                ans = i
        return ans
