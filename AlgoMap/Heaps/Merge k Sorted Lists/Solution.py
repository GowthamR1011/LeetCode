# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        root = ListNode(-1)
        start = root
        top_process = []

        
        for i,node in enumerate(lists):
            if node:
                top_process.append((node.val,i,node))
        
        heapq.heapify(top_process)

        while top_process:
            
            _,index,node = heapq.heappop(top_process)
            root.next = node

            if node.next:
                heapq.heappush(top_process,(node.next.val,index,node.next))

            root = root.next
        
        return start.next

