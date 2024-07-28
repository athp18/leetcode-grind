class TrieNode: # use a trie
    def __init__(self):
        self.children = {}
        self.weight = -1

class WordFilter:
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words 
        self.trie = TrieNode()
        
        for weight, word in enumerate(words):
            long_word = word + '#' + word
            for i in range(len(word) + 1):
                cur = self.trie
                cur.weight = weight
                for j in range(i, len(long_word)):
                    if long_word[j] not in cur.children:
                        cur.children[long_word[j]] = TrieNode()
                    cur = cur.children[long_word[j]]
                    cur.weight = weight

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        cur = self.trie
        search_word = suff + '#' + pref
        for char in search_word:
            if char not in cur.children:
                return -1
            cur = cur.children[char]
        return cur.weight
