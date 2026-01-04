# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.min_depth=float('inf')
        def depth(node,count):
            if not node:
                return
            if not node.left and not node.right:
                self.min_depth=min(self.min_depth,count)
                return
            depth(node.left,count+1)
            depth(node.right,count+1)
        depth(root,1)
        return self.min_depth