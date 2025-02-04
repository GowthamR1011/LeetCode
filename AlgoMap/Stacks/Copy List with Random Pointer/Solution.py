"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        new_head = Node(0)
        visited = {} #original:new   
        new_random = {}
        prev = new_head
        while head:
            new_node = Node(head.val)
            prev.next = new_node

            visited[head] = new_node

            if head.random == None:
                new_node.random = None

            elif head.random in visited:
                new_node.random = visited[head.random]

            else:
                new_random[head] = new_node
            
            prev = prev.next
            head = head.next
        

        for k in new_random:
            new_random[k].random = visited[k.random]


        return new_head.next

            