#lol this is so inelegant it makes my eyes hurt
class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_one(num) -> int:
            count = 0
            for char in num[2:]:  #skip 0b prefix
                if char == '1':
                    count += 1
            return count

        arr = [str(bin(i)) for i in range(n + 1)]
        count1s = [count_one(elem) for elem in arr]
        return count1s
