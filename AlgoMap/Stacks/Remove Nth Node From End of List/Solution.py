# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        n_node = curr= head
        i =1
        while i<=n: 
            n_node = n_node.next
            i += 1

        if n_node == None:
            return head.next

        while curr:
            if n_node.next == None:
                if curr.next != None:
                    curr.next = curr.next.next
                else:
                    curr.next = None
                return head
            
            n_node = n_node.next
            curr = curr.next
        return head