class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
 
        res = []
        stack = []

        def backtrack(ope,close):

            if ope == close == n:
                res.append("".join(stack))
                return 
            
            if ope < n:
                stack.append('(')
                backtrack(ope + 1, close)
                stack.pop()
            
            if close < ope:
                stack.append(')')
                backtrack(ope,close + 1)
                stack.pop()
        
        backtrack(0,0)

        return res