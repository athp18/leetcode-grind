class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = cows = 0
        secret_count = defaultdict(int)
        guess_count = defaultdict(int)

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] += 1
                guess_count[guess[i]] += 1
        
        for digit in guess_count:
            if digit in secret_count:
                cows += min(secret_count[digit], guess_count[digit])
        
        return f"{bulls}A{cows}B"
