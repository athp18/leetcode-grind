# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        heap = [(1, root)]
        heapq.heapify(heap)

        while heap:
            d, n = heapq.heappop(heap)
            if not n.left and not n.right:
                return d
            if n.left:
                heapq.heappush(heap, (d+1, n.left))
            if n.right:
                heapq.heappush(heap, (d+1, n.right))
        return 0
