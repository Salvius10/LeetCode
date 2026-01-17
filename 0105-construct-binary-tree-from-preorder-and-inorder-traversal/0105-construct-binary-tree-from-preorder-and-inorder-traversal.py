# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_pos={}
        for index,val in enumerate(inorder):
            inorder_pos[val]=index
        preorder_index=0
        def build(inorder_left,inorder_right):
            nonlocal preorder_index
            if inorder_left>inorder_right:
                return None
            root_val=preorder[preorder_index]
            preorder_index+=1
            root=TreeNode(root_val)
            root_pos=inorder_pos[root_val]
            root.left=build(inorder_left,root_pos-1)
            root.right=build(root_pos+1,inorder_right)
            return root
        return build(0,len(inorder)-1)