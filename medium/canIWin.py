class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if ((maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal):
            return False
        
        if desiredTotal <= 0:
            return True
        
        memo = {}

        def can_win(choices, total):
            choices = tuple(choices)
            if choices in memo:
                return memo[choices]
            
            # Try all possible moves
            for i in range(len(choices)):
                if choices[i]:
                    if choices[i] >= total or not can_win(choices[:i] + (0,) + choices[i+1:], total - choices[i]):
                        memo[choices] = True
                        return True
            
            # If no winning move, return False
            memo[choices] = False
            return False
        
        return can_win(tuple(range(1, maxChoosableInteger + 1)), desiredTotal)
