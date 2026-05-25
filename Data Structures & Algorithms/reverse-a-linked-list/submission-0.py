# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # approach: methodlogically reverse (order is super important)
        prev = None
        cur = head

        while cur: 
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev

        # # RETRY: 3/8
        # # approach: reverse pointers -- order really matters
        # prev = None
        # cur = head

        # while cur:
        #     temp = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = temp

        # return prev


        # more efficient solution
        # initialize previous as none
        # prev = None
        # curr = head

        # # loop through storing the next node, reverse pointer dir, move forward
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # # prev ends up pointing to "head"
        # return prev

        # FIRST SOLUTION
        # # special case
        # if not head:
        #     return head

        # # get the values of each linked list
        # node = head
        # vals = []
        # while node:
        #     vals.append(node.val)
        #     node = node.next
        
        # # reverse values
        # vals = vals[::-1]
        
        # head = ListNode()
        # node = head
        # for i in range(len(vals)):
        #     node.val = vals[i]
        #     if i < len(vals) - 1:
        #         node.next = ListNode()
        #         node = node.next

        
        # return head