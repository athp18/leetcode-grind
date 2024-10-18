# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        """
        Function that returns our result.
        """
        return self.buildString(root)
    
    def buildString(self, node):
        """
        Build the result string by processing left and right subtrees (an inorder traversal).
        """
        if not node:
            return ""
        result = str(node.val)
        result += self.process_left(node)
        result += self.process_right(node)
        return result
    def process_left(self, node):
        """
        Process left subtree.
        """
        if node.left:
            return "(" + self.buildString(node.left) + ")"
        elif node.right:
            return "()"
        return ""

    def process_right(self, node):
        """
        Process right subtree.
        """
        if node.right:
            return "(" + self.buildString(node.right) + ")"
        return ""
