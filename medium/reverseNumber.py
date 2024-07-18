class Solution:
    def reverse(self, x: int) -> int:
        def check_out_of_bounds(n):
            lower_limit = -2**31
            upper_limit = 2**31 - 1
            if n < lower_limit or n > upper_limit:
                return True
            return False
        if check_out_of_bounds(x):
            return 0
        if x < 0:
            x = abs(x)
            reversed_str = ''.join(reversed(str(x)))
            res = -1 * int(reversed_str)
            if check_out_of_bounds(res):
                return 0
            return res
        res = int(''.join(reversed(str(x)))) 
        if check_out_of_bounds(res):
            return 0
        return res
