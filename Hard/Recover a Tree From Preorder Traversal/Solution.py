# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
 
        tree = []
        curr_count = 0
        curr_number = 0
        
        curr_depth = 0
        for ch in traversal+'-':

            if ch == '-':
                if curr_number > 0:
                   tree.append((curr_number,curr_count))
                   curr_count = 1
                   curr_number = 0
                
                else:
                    curr_count += 1
            else:
                curr_number = curr_number*10 + int(ch)



        stack = []


        for val,d in tree:
            node = TreeNode(val)

            while stack and stack[-1][1] >= d:
                stack.pop()
            
            if stack:
                parent = stack[-1][0]

                if parent.left == None:
                    parent.left = node
                
                else:
                    parent.right = node

            
            else:
                root = node
            
            stack.append((node,d))

        return root
            