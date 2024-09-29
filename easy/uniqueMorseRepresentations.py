class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]

        transformations = {chr(i + 65).lower(): morse[i] for i in range(26)}
        unique = set()
        
        # convert to morse code
        for word in words:
            morse_code = ''.join(transformations[char] for char in word)
            unique.add(morse_code)
        
        return len(unique)
