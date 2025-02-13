class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hashmap = defaultdict(list)

        for word in words:
            if word:
                hashmap[word[0]].append((word, 0))
        
        count = 0
        for c in s:
            old = hashmap[c]
            hashmap[c] = []

            for w, p in old:
                p += 1
                if p == len(w):
                    #reached end of word
                    count += 1
                elif p < len(w):
                    hashmap[w[p]].append((w, p))
        
        return count
