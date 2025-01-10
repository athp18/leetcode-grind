# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []

        def add_subtree(node, dist):
            if not node:
                return
            
            if dist == 0:
                res.append(node.val)
                return
            
            add_subtree(node.left, dist - 1)
            add_subtree(node.right, dist - 1)
        
        def dfs(node, parent):
            if not node:
                return -1
            
            if node == target:
                add_subtree(node, k)
                return 1
            
            left = dfs(node.left, node)
            right = dfs(node.right, node)

            dist = -1
            if left > 0:
                dist = left
                if dist == k:
                    res.append(node.val)
                
                if dist < k:
                    add_subtree(node.right, k - dist - 1)
                
            
            elif right > 0:
                dist = right

                if dist == k:
                    res.append(node.val)
                
                if dist < k:
                    add_subtree(node.left, k - dist - 1)
                
            
            return dist + 1 if dist > 0 else -1
        
        dfs(root, None)
        return res
