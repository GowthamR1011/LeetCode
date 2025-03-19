# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        even = head.next
        node = head.next.next
        while True:

            even.next = node.next
            node.next = odd.next
            odd.next = node

            odd = odd.next
            even = even.next
            if not even:
                break

            node = even.next
            if not node:
                break
        return head

            

           




