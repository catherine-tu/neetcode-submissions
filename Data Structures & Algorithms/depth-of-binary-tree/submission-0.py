# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # approach: recursion -- count children and add 1, find the max
        def depth(node):
            if not node:
                return 0
            return 1 + max(depth(node.right), depth(node.left))
        
        return depth(root)

        # # data structure: list of tuples, [(node, depth), ...]
        # # track final depths in a seperate set
        # # return largest depth
        # visiting = [(root, 1)]
        # depth_set = set()

        # # special case: empty tree
        # if not root:
        #     return 0

        # while visiting:
        #     node, dep = visiting.pop()

        #     # if not does not have children
        #     if not (node.left or node.right):
        #         depth_set.add(dep)

        #     # +1 if has children
        #     if node.left:
        #         visiting.append((node.left, dep + 1))
        #     if node.right:
        #         visiting.append((node.right, dep + 1))

        # # after traversing
        # return max(depth_set)