# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.first = None
        self.prev = None
        self.middle = None
        self.last = None

    def inorder(self, root):
        if not root:
            return
        
        # traverse the left subtree
        self.inorder(root.left)
        
        # check for swapped nodes
        if self.prev and root.val < self.prev.val:
            if not self.first:
                # first occurrence
                self.first = self.prev
                self.middle = root
            else:
                # second occurrence
                self.last = root
        
        # update previous node
        self.prev = root
        
        # traverse the right subtree
        self.inorder(root.right)
    
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # initialize the variables
        self.first = None
        self.middle = None
        self.last = None
        self.prev = TreeNode(float('-inf'))  # use a very small value to start with
        
        # perform in-order traversal
        self.inorder(root)
        
        # swap the values of the nodes to recover the tree
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val
