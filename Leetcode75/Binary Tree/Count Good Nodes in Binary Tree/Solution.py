# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
    
    def dfs(self,node,minm):
         
        if node.val >= minm:
            self.count += 1
            minm = node.val
        

        if node.left: self.dfs(node.left,minm)
        if node.right: self.dfs(node.right,minm)
        
    def goodNodes(self, root: TreeNode) -> int:
        
        self.dfs(root,root.val)
      
        return self.count