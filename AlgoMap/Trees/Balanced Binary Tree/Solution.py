# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def height(node):

            if node == None:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                self.result = False
            
            return max(left_height,right_height) + 1
        
        height(root)
        return self.result
