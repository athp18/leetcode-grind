class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            return word == word[::-1]
        word_dict = {
            word: i for i, word in enumerate(words)
        }
        res = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n+1):
                prefix = word[:j]
                suffix = word[j:]

                if isPalindrome(prefix):
                    rev_suffix = suffix[::-1]
                    if rev_suffix in word_dict and word_dict[rev_suffix] != i:
                        res.append([word_dict[rev_suffix], i])
                if j != n and isPalindrome(suffix):
                    rev_prefix = prefix[::-1]
                    if rev_prefix in word_dict and word_dict[rev_prefix] != i:
                        res.append([i, word_dict[rev_prefix]])
        return res
