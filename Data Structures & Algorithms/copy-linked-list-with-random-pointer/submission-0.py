"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # mapping old to new
        # copy each node of original 
        deep = dict()

        node = head 
        while node is not None:
            deep[node] = Node(node.val)
            node = node.next
        
        # copy over deep pointers
        node = head 
        while node is not None:
            # copy over the next pointer
            deep[node].next = deep[node.next] if node.next else None 
            # random pointer
            deep[node].random = deep[node.random] if node.random else None
            node = node.next
        
        return None if not deep else deep[head]
        
        # # approach: use a hash function first to remember node mappings @ indexes (make dupes)
        # # then traverse and add pointers 

        # # hash map creating new dupe nodes associated with each one
        # node = head
        # values = dict()
        # while node:
        #     values[node] = Node(node.val)
        #     node = node.next

        # # go through map and map the pointers 
        # node = head
        # while node:
        #     # next 
        #     if node.next:
        #         values[node].next = values[node.next]
        #     # random
        #     if node.random:
        #         values[node].random = values[node.random]

        #     node = node.next
        
        # return values[head] if values else None # special case: if empty, return none