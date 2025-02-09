# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        self.count = k
        self.result = -1
        
        def inorder(node):
            
            if node == None:
                return
            
            inorder(node.left)
            
            if self.count == 1:
                self.result = node.val
            
            self.count -=1 
            if self.count >= 1:

                inorder(node.right)
            
        inorder(root)
        return self.result
        
