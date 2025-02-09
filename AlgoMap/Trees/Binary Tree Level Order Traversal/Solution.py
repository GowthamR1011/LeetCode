# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        que = deque([(root,0)])
        
        result = []
        while que:

            node,level = que.popleft()
            if level < len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
                


            if node.left: que.append((node.left,level+1))
            if node.right: que.append((node.right,level+1))

        return result