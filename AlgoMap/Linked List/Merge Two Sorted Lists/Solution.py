# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if l1 == None:
            return l2
        if l2 == None:
            return l1
            
        if l1.val < l2.val:
            head_result = l1
            l1 = l1.next
        else:
          head_result = l2
          l2 = l2.next

        result = head_result

        while l1!=None and l2!=None:

            if l1.val < l2.val:
            
                result.next = l1
                result = result.next
                l1 = l1.next

            else:

                result.next = l2
                result = result.next
            
                l2 = l2.next
            
        if l2:
            result.next = l2
        if l1:
            result.next = l1

            

        return head_result