# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        result=[]
        while stack:
            level_size=len(stack)
            for i in range(level_size):
                current=stack.pop(0)
                if i==level_size-1:
                    result.append(current.val)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        return result
            
            