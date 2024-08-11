class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0, 0
        for i, j in zip(s1, s2):
            if i != j:
                if i == 'x':
                    xy += 1
                else:
                    yx += 1
        if (xy + yx) % 2 != 0:
            return -1
        return xy // 2 + yx // 2 + (xy%2) * 2
