# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        dummy=TreeNode(0)
        
        temp=dummy
        def helper(root):
            nonlocal temp
            if not root:
                return
            helper(root.left)
            root.left=None
            temp.right=root
            temp=root
            helper(root.right)
        helper(root)
        return dummy.right