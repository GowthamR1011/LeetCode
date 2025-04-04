# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(node):

            if not node:
                return (None,0)
            
            l_lca, l_lvl = dfs(node.left)
            r_lca, r_lvl = dfs(node.right)
            
            
            if r_lvl == l_lvl:
                return (node,r_lvl + 1)
            elif r_lvl > l_lvl:
                return (r_lca,r_lvl + 1)
            else:
                return (l_lca,l_lvl + 1)

        return dfs(root)[0]
        
