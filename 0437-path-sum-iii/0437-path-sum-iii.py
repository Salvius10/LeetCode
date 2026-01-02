# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,currSum):
            if not root:
                return 
            currSum+=root.val
            self.count+=prefix.get(currSum-targetSum,0)
            prefix[currSum]=prefix.get(currSum,0)+1
            dfs(root.left,currSum)
            dfs(root.right,currSum)
            prefix[currSum]-=1

        prefix={0:1}
        self.count=0
        dfs(root,0)
        return self.count