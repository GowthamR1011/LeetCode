# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if not root:
            return []
        q = deque()

        q.append((0,root))

        while q:
            lev , node = q.popleft()
            if not q or q[0][0]!= lev:
                res.append(node.val)
            if node.left:  q.append((lev + 1,node.left))
            if node.right : q.append((lev + 1, node.right))

        
        return res


# Time complexity: O(N)
# Space complexity: O(N)