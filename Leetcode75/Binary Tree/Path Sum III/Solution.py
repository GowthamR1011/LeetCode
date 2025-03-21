# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        
        self.prefix_sum = defaultdict(int)

    def dfs(self,node,curr,targetSum):
        
        if not node:
            return 0
        

        curr += node.val

        res = self.prefix_sum[curr - targetSum]

        self.prefix_sum[curr] += 1

        res += self.dfs(node.left,curr,targetSum)
        res += self.dfs(node.right,curr,targetSum)

        self.prefix_sum[curr] -= 1

        return res

        

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.prefix_sum[0] = 1
        return self.dfs(root,0,targetSum)