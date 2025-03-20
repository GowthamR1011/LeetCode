# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaf1, leaf2 = [],[]

        s = [root1]

        while s:

            n = s.pop()

            if not n.left and not n.right:
                leaf1.append(n.val)
            
            if n.left: s.append(n.left)
            if n.right: s.append(n.right)
        
        count = 0
        s = [root2] 

        while s:
            n = s.pop()

            if not n.left and not n.right:
                if count<len(leaf1) and leaf1[count] == n.val:
                    count += 1
                else:

                    return False
            
            if n.left: s.append(n.left)
            if n.right: s.append(n.right)
        
        return count == len(leaf1)
                
            



        