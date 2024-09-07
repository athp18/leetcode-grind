class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def update(index, val):
            while index < len(bit):
                bit[index] += val
                index += index & -index

        def query(index):
            total = 0
            while index > 0:
                total += bit[index]
                index -= index & -index
            return total

        def find_kth_one(k):
            left, right = 1, len(bit) - 1
            while left < right:
                mid = (left + right) // 2
                if query(mid) < k:
                    left = mid + 1
                else:
                    right = mid
            return left

        n = len(people)
        bit = [0] * (n + 1)
        for i in range(1, n + 1):
            update(i, 1)

        people.sort(key=lambda x: (x[0], -x[1]))
        res = [None] * n

        for h, k in people:
            pos = find_kth_one(k + 1)
            res[pos - 1] = [h, k]
            update(pos, -1)

        return res
