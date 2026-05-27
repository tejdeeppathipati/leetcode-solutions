# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# dfs - 
# bottom up 
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def checkgoodNode(node, max_val):
            if not node:
                return 

            nonlocal res

            max_val = max(node.val, max_val)

            if node.val >= max_val:
                res += 1
                
            checkgoodNode(node.left, max_val)
            checkgoodNode(node.right, max_val)

        checkgoodNode(root, root.val)
        return res
