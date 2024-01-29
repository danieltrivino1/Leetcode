# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        result = 0

        prev = None
        curr = copy.deepcopy(head)

        length = 0

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

            length += 1

        print(head)
        for _ in range(length//2):
            result = max(result, head.val + prev.val)
            head = head.next
            prev = prev.next

        return result
        

        
        
