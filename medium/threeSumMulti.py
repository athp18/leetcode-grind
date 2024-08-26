class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1
            
        keys = sorted(count)
        result = 0

        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else:  # x+y+z == target
                    if i < j < k:
                        result += count[x] * count[y] * count[z]
                    elif i == j < k:
                        result += count[x] * (count[x] - 1) // 2 * count[z]
                    elif i < j == k:
                        result += count[x] * count[y] * (count[y] - 1) // 2
                    else:  # i == j == k
                        result += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                    j += 1
                    k -= 1

        return result % MOD
