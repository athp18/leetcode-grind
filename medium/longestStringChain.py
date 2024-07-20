class Solution(object): # gn. we gon make it :) :)
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        longest = {}
        max_len = 1

        for w in words:
            curr = 1
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]
                if pred in longest:
                    curr = max(curr, longest[pred] + 1)
            longest[w] = curr
            max_len = max(max_len, curr)

        return max_len
