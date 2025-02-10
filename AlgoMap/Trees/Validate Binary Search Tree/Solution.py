# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        self.result = True

        def checkBST(node):

            if node == None:
                return 
            
            if self.result:
                checkBST(node.left)

            if self.prev != None:
                if(self.prev >=node.val):
                    self.result = False
            
            self.prev = node.val

            if self.result:
                checkBST(node.right)
        
        checkBST(root)
        return self.result