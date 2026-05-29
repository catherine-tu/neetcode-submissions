# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # check the greater & less than values
        while True:
            # if root is greater than both:
            if root.val > p.val and root.val > q.val:
                root = root.left
            # if root smaller than both:
            elif root.val < p.val and root.val < q.val: 
                root = root.right 
            # else
            else:
                return root


        # # APPROACH: BST -- find a z such that children x and y intersect that value

        # while True:
        #     # if root is greater than both
        #     if root.val > p.val and root.val > q.val:
        #         root = root.left
        #     # if root is smaller than both, move right
        #     elif root.val < p.val and root.val < q.val:
        #         root = root.right
        #     # found closest ancestor - BST property
        #     else:
        #         return root