from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def is_prefix_and_suffix(prefix, word):
            return word.startswith(prefix) and word.endswith(prefix)
        n = len(words)
        count = 0
    
        for i in range(n):
            for j in range(i + 1, n):
                if is_prefix_and_suffix(words[i], words[j]):
                    count += 1
    
        return count
