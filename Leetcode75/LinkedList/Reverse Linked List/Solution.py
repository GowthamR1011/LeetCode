# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = head
        if not head or not head.next:
            return head
        
        node = head.next

        while node:
            
            nex = node.next
            node.next = prev
            prev = node

            node = nex
        head.next = None

        return prev





