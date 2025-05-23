# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):

            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            

            return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        

        def has_subRoot(node):

            if not node:
                return False
            
            return isSameTree(node,subRoot) or has_subRoot(node.left) or has_subRoot(node.right)
        

        return has_subRoot(root)
