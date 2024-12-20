class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:  
            return n
            
        MOD = 10**9 + 7
        BASE = 31
        
        power = [1]
        for i in range(n):
            power.append((power[-1] * BASE) % MOD)
            
        prefix = [0]
        for c in s:
            prefix.append((prefix[-1] * BASE + ord(c) - ord('a')) % MOD)
            
        dp = [1] * n
        for i in range(n-2, -1, -1):
            max_len = (n - i) // 2

            found_valid = False
            for length in range(1, max_len + 1):
                if i + 2*length > n:
                    break
                    
                h1 = (prefix[i+length] - prefix[i] * power[length]) % MOD
                h2 = (prefix[i+2*length] - prefix[i+length] * power[length]) % MOD
                
                if h1 == h2 and s[i:i+length] == s[i+length:i+2*length]:
                    dp[i] = max(dp[i], 1 + dp[i + length])
                    found_valid = True
            
            if not found_valid:
                dp[i] = 1
                
        return dp[0]
