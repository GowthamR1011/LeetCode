# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        ind_node = {}
        idx = 0
        node = head

        while node:
            ind_node[idx] = node
            idx += 1
            node = node.next
        


        head = ListNode()
        node = head
        l = 0
        r = idx - 1

        while l<r:

            node.next = ind_node[l]
            node = node.next


            node.next = ind_node[r]
            node = node.next
            
            l += 1
            r -= 1
        
        if l == r:
            node.next = ind_node[l]
            node = node.next
        
        node.next = None

        
        head = head.next

        