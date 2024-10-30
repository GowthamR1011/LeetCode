'''
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
                
        temp = ListNode(0,head)

        head = temp

        curr = head

        while curr:

            curr.val = (curr.val *2 ) % 10 

            if curr.next and curr.next.val > 4:
                curr.val = curr.val + 1 
            
            curr = curr.next 
        
        if head.val == 0:
            head = head.next
        
        return head
    

'''
This is a better solution. The program only traversese through the LinkedList once. Not forming a new linked (Compared to prev solution)
also makes the solution more memory efficient. 
'''