# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        if root.left == None and root.right == None:
            if targetSum-root.val == 0:
                self.result = True
        
        
        self.hasPathSum(root.left,targetSum-root.val)
        self.hasPathSum(root.right,targetSum-root.val)

        
        return self.result
        