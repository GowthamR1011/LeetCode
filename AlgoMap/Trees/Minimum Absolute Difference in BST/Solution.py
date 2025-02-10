# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.prev = None
        self.min = inf


        def difference(node):

            if not node:
                return
            
            difference(node.left)
            if self.prev != None:
                if abs(node.val-self.prev)<self.min:
                    self.min = abs(node.val-self.prev)
            
            self.prev = node.val
        
            difference(node.right)
        
        difference(root)
        return self.min
            

