# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.result = root

        def checkNodeinTree(node,p,q):
            if node == None:
                return 
            
            if node.val == p.val or node.val == q.val:
                self.result = node
            
            elif node.val > p.val and node.val < q.val:
                self.result = node
            
            elif node.val < p.val and node.val > q.val:
                self.result = node

            
            elif node.val < p.val:
                checkNodeinTree(node.right,p,q)
            
            else:
                checkNodeinTree(node.left,p,q)


        checkNodeinTree(root,p,q)
        return self.result


        

                

        

        