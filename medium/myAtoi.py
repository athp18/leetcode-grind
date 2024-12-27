class Solution:
    def myAtoi(self, s: str) -> int:
        i, n, sign, res = 0, len(s), 1, 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        if s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if res > INT_MAX or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN

            res = res * 10 + digit
            i += 1

        res *= sign
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res 


                
                
