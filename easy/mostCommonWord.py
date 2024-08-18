class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split()

        hashmap = {}
        for w in words:
            word = w.lower().strip("!?',;.")
            if word not in banned:
                if word in hashmap:
                    hashmap[word] += 1
                else:
                    hashmap[word] = 1
        res = ""
        max_so_far = 0
        for k, v in hashmap.items():
            if v > max_so_far:
                res = k
                max_so_far = max(v, max_so_far)
        return res
                
