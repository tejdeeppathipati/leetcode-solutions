# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            root = self.replaceNode(root)

        return root

    def replaceNode(self, root: Optional[TreeNode]):
        #1. no child node
        #2. one child node - replace with child node
        # 3. two child node - right subtree smallest node
        if not root.right and not root.left:
            return None

        elif not root.right and root.left:
            return root.left

        elif root.right and not root.left:
            return root.right

        else:
            smallest_node = root.right
            while smallest_node.left:
                smallest_node = smallest_node.left
            
            root.val = smallest_node.val
            root.right = self.deleteNode(root.right, smallest_node.val)

            return root