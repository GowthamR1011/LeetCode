# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        n_node = node
        for _ in range(n):
            n_node = n_node.next
        
        if n_node == None:
            return node.next
        
        while n_node.next:
            node = node.next
            n_node = n_node.next
        

        node.next = node.next.next

        return head
