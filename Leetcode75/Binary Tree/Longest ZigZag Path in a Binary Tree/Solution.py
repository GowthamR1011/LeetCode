# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
    
    def dfs(self,node, direc,l):

            if not node: 
                return 
            
            self.res = max(self.res,l)

            if direc:
                self.dfs(node.left,0,l+1)
                self.dfs(node.right,1,1)
        
            else:
                self.dfs(node.left,0,1)
                self.dfs(node.right,1,l+1)
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        self.dfs(root.left,0,1)
        self.dfs(root.right,1,1)

        return self.res
    
                    




            
