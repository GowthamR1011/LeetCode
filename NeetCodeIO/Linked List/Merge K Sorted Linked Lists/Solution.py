# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def getMinNode(self,nodes):
        minNode = ListNode(float("infinity"))
        minIndex = -1

        for i in range(len(nodes)):
            if nodes[i] and  nodes[i].val < minNode.val:
                minNode = nodes[i]
                minIndex = i
        return minNode, minIndex
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        k = len(lists)

        head = ListNode(0)

        node = head

        while any([l != None for l in lists]):

            minNode,minIndex  = self.getMinNode(lists)
            
            node.next = minNode

            node = minNode
            lists[minIndex] = lists[minIndex].next
        
        return head.next
            

