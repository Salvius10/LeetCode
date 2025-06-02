# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1=[p]
        queue2=[q]
        while queue1 and queue2:
            nodep=queue1.pop(0)
            nodeq=queue2.pop(0)
            if not nodep and not nodeq:
                continue
            if not nodep or not nodeq:
                return False
            if nodep.val!=nodeq.val:
                return False
            queue1.append(nodep.left)
            queue1.append(nodep.right)
            queue2.append(nodeq.left)
            queue2.append(nodeq.right)
        return not queue1 and not queue2