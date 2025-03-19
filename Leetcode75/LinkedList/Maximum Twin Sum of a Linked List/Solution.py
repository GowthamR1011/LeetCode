# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        val = []
 
        while head:
            val.append(head.val)
            head = head.next
        
        maxm = 0
        n = len(val)
        for i in range(n//2):
            maxm = max(maxm,val[i] + val[n-1-i])
        
        return maxm