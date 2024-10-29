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
        agg = head
        total_val = 0
        while agg != None:
            total_val = total_val*10 + agg.val
            agg = agg.next

        
        total_val = total_val * 2
        prev_node = ListNode(total_val%10)
        total_val = total_val // 10

        while total_val > 0:
            new_node = ListNode(total_val%10,prev_node)

            total_val = total_val // 10
            prev_node = new_node
        

        return prev_node