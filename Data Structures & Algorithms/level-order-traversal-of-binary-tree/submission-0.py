# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use indexes as depth
        out = []

        def levels(node, level):
            if not node:
                return
            
            # start a new level if needed
            if len(out) <= level:
                out.append([])
            # add current level nodes
            out[level].append(node.val)

            levels(node.left, level + 1)
            levels(node.right, level + 1)
        
        levels(root, 0)
        return out


        # # approach: use indexing to track which level we are on

        # out = []
        
        # def levels(node, level):

        #     if not node:
        #         return

        #     # start a new level
        #     if len(out) <= level:
        #         out.append([])

        #     # append current
        #     out[level].append(node.val)

        #     # recurse
        #     levels(node.left, level + 1)
        #     levels(node.right, level + 1)

        # levels(root, 0)
        # return out