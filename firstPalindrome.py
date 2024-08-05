class Solution: 
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            l = len(s) # divide string length by 2 and check if the first half of the string and reversed second half are equivalent. O(n) time complexity
            return s[:l // 2] == s[(l + 1) // 2:][::-1]

        for word in words: # O(n) time complexity
            if isPalindrome(word):
                return word

        return "" # O(n) time complexity, O(1) space complexity
