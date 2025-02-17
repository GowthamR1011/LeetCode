"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visit = {}
        
        if node is None:
            return None
        stack = [node]

        while len(stack) > 0:

            curr = stack.pop()
            new = Node(curr.val)

            visit[curr] = new

            for nei in curr.neighbors:
                if nei not in visit and  nei != None:
                    stack.append(nei)

        for k in visit:
            for nei in k.neighbors:
                visit[k].neighbors.append(visit[nei])


        return visit[node]