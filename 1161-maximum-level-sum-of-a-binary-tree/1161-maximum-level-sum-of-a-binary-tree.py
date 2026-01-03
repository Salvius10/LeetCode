# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum=float('-inf')
        stack=[root]
        max_level=1
        level=1
        while stack:
            level_size=len(stack)
            sum_val=0
            for i in range(level_size):
                current=stack.pop(0)
                sum_val=sum_val+current.val
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
            if sum_val > max_sum:
                max_sum = sum_val
                max_level = level
            level+=1
        return max_level
            