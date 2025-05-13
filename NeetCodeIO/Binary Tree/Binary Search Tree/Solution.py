# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.res = True
        def dfs(node,minm, maxm):

            if not node:
                return 
            

            if minm < node.val < maxm:
                
                dfs(node.left, minm, node.val)
                dfs(node.right, node.val, maxm)

            else:
                self.res = False
                return 


        dfs(root,-float("infinity"), float("infinity"))
        return self.res
        
