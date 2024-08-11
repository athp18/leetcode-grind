class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = {}
        for w in words:
            if w in hashmap:
                hashmap[w] += 1
            else:
                hashmap[w] = 1

        ans, mid = 0, False
        for word, count in hashmap.items():
            if word[0] == word[1]:  # Palindromic word
                if count % 2 == 0:
                    ans += count * 2
                else:
                    ans += (count - 1) * 2
                    mid = True
            elif word[::-1] in hashmap:
                ans += min(count, hashmap[word[::-1]]) * 4
                hashmap[word[::-1]] = 0  #avoid counting twice
        if mid:
            ans += 2

        return ans
