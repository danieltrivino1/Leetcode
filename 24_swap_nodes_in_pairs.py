# 24. Swap Nodes in Pairs
# Solution (Linked list):

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        dummy = head.next

        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head

            next_node = head.next.next
            head.next.next = head
            head.next = next_node
            head = next_node
        
        return dummy
      
