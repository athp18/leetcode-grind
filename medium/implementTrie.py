class Node:
    def __init__(self):
        self.terminal = False
        self.children = [None] * 26

class PrefixTree:
    def __init__(self):
        self.root = Node()
    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            index = ord(char) - ord('a')
            if current.children[index] is None:
                current.children[index] = Node()
            current = current.children[index]
        current.terminal = True
    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            i = ord(char) - ord("a")
            if current.children[i] == None:
                return False
            current = current.children[i]
        return current.terminal
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            i = ord(char) - ord("a")
            if current.children[i] is None:
                return False
            current = current.children[i]
        return True
