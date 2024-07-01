# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive approach

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float('-inf')
        high = float('inf')
        if not root:
            return True # still satisfies BST properties
        def validate(root, low, high):
            if not root:
                return True
            if not (low < root.val < high): # means that the value of the root is not between low and high, i.e. is OOB
                return False
            l_valid = validate(root.left, low, root.val) # means that the value of the left node is between low and the value of the node
            r_valid = validate(root.right, root.val, high) # means that the value of the right node is between the value of the root and high
            return l_valid and r_valid # means both right and left are valid
        return validate(root, low, high)
