# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # TRY AGAIN
        # approach: continue while we are < len - n
        # count the length of linked list
        temp = head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        
        # special case: remove head
        if n == length:
            return head.next

        # get to the nth node we must remove
        i = 0
        temp = head
        while i < length-n-1:
            temp = temp.next
            i += 1
        
        # remove and reorg
        temp.next = temp.next.next
        return head



        # # initial approach: counting length in one pass, then remove len - n node
        
        # cur = head
        # leng = 0
        # # get length of LL
        # while cur:
        #     cur = cur.next
        #     leng += 1
        
        # # remove when n - leng
        # if n == leng:
        #     return head.next

        # cur = head
        # i = 0
        # while cur:
        #     # remove
        #     if leng - i - 1 == n:
        #         tmp = cur.next
        #         cur.next = cur.next.next
        #         tmp.next = None
            
        #     cur = cur.next
        #     i += 1
        
        # return head

        