# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._inorder_helper(root, result)
        return result
    def _inorder_helper(self, node, result):
        if not node:
            return
        self._inorder_helper(node.left, result)
        result.append(node.val)
        self._inorder_helper(node.right, result)
