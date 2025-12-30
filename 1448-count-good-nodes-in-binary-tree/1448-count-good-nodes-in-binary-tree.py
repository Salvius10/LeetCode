# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue=[(root,root.val)]
        count=0
        while queue:
            current,max_so_far=queue.pop(0)
            if current.val>=max_so_far:
                count+=1
            new_max=max(max_so_far,current.val)
            if current.left:
                queue.append((current.left,new_max))
            if current.right:
                queue.append((current.right,new_max))
        return count