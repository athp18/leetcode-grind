# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            if node.val > self.first_min and node.val < self.second_min:
                self.second_min = node.val
            elif node.val > self.second_min and self.second_min == float('inf'):
                self.second_min = node.val
            inorder(node.right)
        
        if not root:
            return -1
        
        self.first_min = root.val
        self.second_min = float('inf')
        
        inorder(root)
        
        return self.second_min if self.second_min < float('inf') else -1

        
