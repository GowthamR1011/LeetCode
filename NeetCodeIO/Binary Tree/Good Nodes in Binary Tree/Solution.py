# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        self.res = 0


        def dfs(node,maxm):

            if not node:
                return 
            

            if node.val >= maxm:
                self.res += 1
                maxm = node.val
            

            dfs(node.left, maxm)
            dfs(node.right,maxm)
        
        if not root:
            return 0

        dfs(root,root.val)
        return self.res

