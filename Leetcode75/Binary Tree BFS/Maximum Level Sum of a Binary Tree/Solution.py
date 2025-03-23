# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        

        q = deque([(0,root)])
        curr_level, curr_sum, max_sum,max_lev= 0,0,-inf,0

        while q:

            level, node = q.popleft()
            
            if curr_level == level:
                curr_sum += node.val
            else:
                if curr_sum > max_sum:
                    max_sum = curr_sum 
                    max_lev = curr_level

                curr_level = level
                curr_sum = node.val
            
            if node.left: q.append((level+ 1,node.left))
            if node.right: q.append((level+1,node.right))
    
        if curr_sum > max_sum:
            max_lev = level
        
        return max_lev + 1