class Solution(object):
    def compress(self, chars):
        """
        Compress the list of characters in-place and return the new length.
        :type chars: List[str]
        :rtype: int
        """
        if not chars:
            return 0
        
        write = read = 0
        n = len(chars)
        
        while read < n:
            current_char = chars[read]
            count = 1
            while read + 1 < n and chars[read] == chars[read + 1]:
                read += 1
                count += 1
            chars[write] = current_char
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            read += 1
        
        # If needed, truncate the list to the new length
        # This step is optional depending on the use case
        while len(chars) > write:
            chars.pop()
        
        return write
