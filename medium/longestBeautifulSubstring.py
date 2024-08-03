class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        MAX = 0
        curr = 0
        vowels = set()
        prev = ''

        for i, char in enumerate(word):
            if i > 0 and char < word[i - 1]:
                curr = 0
                vowels.clear()
            
            curr += 1
            vowels.add(char)

            if len(vowels) == 5:
                MAX = max(MAX, curr)
        
        return MAX
