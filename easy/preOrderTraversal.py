# Preorder traversal: visit all left subtrees, then all right subtrees
# This solution has a time complexity of O(n) and a space complexity of O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        final = []
        final.append(root.val)
        final.extend(self.preorderTraversal(root.left))
        final.extend(self.preorderTraversal(root.right))
        return final
