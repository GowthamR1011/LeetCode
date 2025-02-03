# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        x = head
        prev = head
        while x:
            next_node = x.next
            if x == head:
                x.next = None
            else:
                x.next = prev   
            prev = x
            x = next_node
        return prev





