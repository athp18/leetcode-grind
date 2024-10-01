# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node, SUM):
            if not node:
                return SUM
            
            SUM = inorder(node.right, SUM)
            SUM += node.val
            node.val = SUM

            SUM = inorder(node.left, SUM)
            return SUM
        
        inorder(root, 0)
        return root
