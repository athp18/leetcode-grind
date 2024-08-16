class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n, operations = len(word), 0
        
        while True:
            operations += 1
            if word[k*operations:] == word[:n-k*operations]:
                return operations
            if k * operations >= n:
                return operations
