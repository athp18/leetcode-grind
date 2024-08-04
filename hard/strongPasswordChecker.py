class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        required = int(not has_lower) + int(not has_upper) + int(not has_digit)
        replace = 0
        one = two = 0
        i = 2

        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                
                replace += length // 3
                
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            else:
                i += 1
        if n < 6:
            return max(required, 6 - n)
        elif n <= 20:
            return max(required, replace)
        else:
            delete = n - 20
            
            replace -= min(delete, one * 1) // 1
            replace -= min(max(delete - one, 0), two * 2) // 2
            replace -= max(delete - one - 2 * two, 0) // 3
            
            return delete + max(required, replace)
