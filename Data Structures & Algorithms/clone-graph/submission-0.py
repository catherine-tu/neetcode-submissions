"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # approach: have a dictionary mapping old -> new nodes, then go through and create deep copy

        if not node: #edge case 
            return None

        mappings = dict()
        # create new nodes, worry about neighbors later!
        def copy_nodes(node):
            if node and node not in mappings:
                mappings[node] = Node(node.val)
                for nn in node.neighbors:
                    copy_nodes(nn)

        copy_nodes(node)
        
        # now, go through and add neighbors
        for old_node in mappings:
            for neighbors in old_node.neighbors:
                mappings[old_node].neighbors.append(mappings[neighbors])
        
        return mappings[node]




        # # traverse through using recursive dfs

        # if not node:
        #     return None
        
        # visited = {} # dict of clone nodes

        # def dfs(v):
        #     if v in visited:
        #         return visited[v]
            
        #     clone = Node(v.val)
        #     visited[v] = clone 

        #     # loop through neighbors and append neighbors neighbors, etc
        #     for neighbor in v.neighbors:
        #         clone.neighbors.append(dfs(neighbor))
        #     return clone

        # return dfs(node)
