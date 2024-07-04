class Node:
    def __init__(self):
        self.terminal = False
        self.children = [None] * 26

class WordDictionary:

    def __init__(self):
        self.root = Node()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                current.children[index] = Node()
            current = current.children[index]
        current.terminal = True
        
    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.terminal
            if word[i] == '.':
                for child in node.children:
                    if child is not None and dfs(child, i + 1):
                        return True
            else:
                index = ord(word[i]) - ord('a')
                if node.children[index] is not None:
                    return dfs(node.children[index], i + 1)
            return False
        
        return dfs(self.root, 0)
