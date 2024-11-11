class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Unique identifiers for certain even and odd numbers
        hashmap_even = {
            "z": 0,  # zero
            "w": 2,  # two
            "u": 4,  # four
            "x": 6,  # six
            "g": 8   # eight
        }
        hashmap_odd = {
            "o": 1,  # one (after zero, two, four removed)
            "h": 3,  # three (after eight removed)
            "f": 5,  # five (after four removed)
            "s": 7,  # seven (after six removed)
            "i": 9   # nine (after five, six, eight removed)
        }
        
        # Initialize counter
        counter = {i: 0 for i in range(10)}
        
        # Count the occurrences of each character in s
        char_count = {}
        for a in s:
            char_count[a] = char_count.get(a, 0) + 1

        # Count even digits based on unique characters
        for char, digit in hashmap_even.items():
            if char in char_count:
                counter[digit] = char_count[char]

        # Adjust for odd digits based on updated character counts
        counter[1] = char_count.get('o', 0) - counter[0] - counter[2] - counter[4]
        counter[3] = char_count.get('h', 0) - counter[8]
        counter[5] = char_count.get('f', 0) - counter[4]
        counter[7] = char_count.get('s', 0) - counter[6]
        counter[9] = char_count.get('i', 0) - counter[5] - counter[6] - counter[8]
        
        # Build the result
        res = []
        for k, v in counter.items():
            res += str(k) * v
        return ''.join(sorted(res))
