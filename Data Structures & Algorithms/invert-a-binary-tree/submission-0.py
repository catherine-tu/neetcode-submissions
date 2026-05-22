# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # ROOTS FIRST THEN LEAFS
        if not root:
            return None
        
        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root

        # LEAF FIRST then ROOTS
        # if not root:
        #     return None
        
        # # recursion
        # def tree(node):
        #     if not node:
        #         return None

        #     # reach leaf then reverse
        #     left = tree(node.left)
        #     right = tree(node.right)

        #     node.left = right
        #     node.right = left

        #     return node

        # return tree(root)


        # # approach: recurse symmetrically and swap
        # def tree(root):
        #     # base case -- root = None
        #     if (not root):
        #         return None
        #     # get left and right sides
        #     left = tree(root.left)
        #     right = tree(root.right)

        #     # swap left and right
        #     root.left = right
        #     root.right = left
            
        #     return root

        # return tree(root)
            