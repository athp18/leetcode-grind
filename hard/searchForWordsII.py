from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def add(self, word):
        cur = self
        cur.refs += 1
        for char in word:
            if char not in cur.children:
                cur.children[char] = Trie()
            cur = cur.children[char]
            cur.refs += 1
        cur.isWord = True

    def remove(self, word):
        cur = self
        cur.refs -= 1
        for char in word:
            if char in cur.children:
                next_node = cur.children[char]
                next_node.refs -= 1
                if next_node.refs == 0:
                    del cur.children[char]
                    return
                cur = next_node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()
        for w in words:
            root.add(w)
        rows, cols = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] not in node.children or
                node.children[board[r][c]].refs < 1 or
                (r, c) in visit
            ):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.remove(word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        return list(res)
