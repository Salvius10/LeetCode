# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1)==self.get_leaves(root2) 

    def get_leaves(self,root):
        leaves=[]
        self.dfs(root,leaves)
        return leaves

    def dfs(self,root,leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        self.dfs(root.left,leaves)
        self.dfs(root.right,leaves)

