# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root:
            if val > root.val:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
        else:
            root = TreeNode(val)
        return root
        