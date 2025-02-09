# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def checkTree(node,subRoot):
            if node == None and subRoot == None:
                return True
            if node == None or subRoot == None:
                return False

            if node.val == subRoot.val:
                return True and checkTree(node.left,subRoot.left) and checkTree(node.right,subRoot.right)

            return False
        

        if root == None:
            return False
        
        if checkTree(root,subRoot):
            return True
        
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)