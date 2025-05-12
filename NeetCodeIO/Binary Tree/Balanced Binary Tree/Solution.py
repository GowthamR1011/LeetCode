# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def dfs(node):

            if not node:
                return 0


            l = dfs(node.left)
            r = dfs(node.right)

            self.result = self.result and (abs(l-r) < 2)

            return max(l+1, r+1)
        
        _ = dfs(root)

        return self.result

