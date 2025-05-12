# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        
        
        def dfs(node,d):

            if not node:
                return 
            
            self.max_depth = max(d, self.max_depth)
            dfs(node.left,d + 1)
            dfs(node.right,d + 1)
        
        dfs(root, 1)
        return self.max_depth