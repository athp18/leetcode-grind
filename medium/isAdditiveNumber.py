class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            if num[0] == '0' and i > 1:
                break
            for j in range(i + 1, n):
                if num[i] == '0' and j - i > 1:
                    break
                
                a, b = int(num[:i]), int(num[i:j])
                k = j
                while k < n:
                    c = a + b
                    c_str = str(c)

                    if not num.startswith(c_str, k):
                        break
                    k += len(c_str)
                    a, b = b, c
                
                if k == n:
                    return True
        return False
