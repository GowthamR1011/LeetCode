class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        self.sol = ""

        def backtrack(index):

            if len(self.sol) == 2*n:
                res.append(self.sol)
                return

            for i in range(index,len(self.sol)):
                if i == len(self.sol)-1:
                    self.sol = self.sol + '()'
                    backtrack(i+1)
                    self.sol = self.sol[:len(self.sol)-2]

                else:
                    self.sol = self.sol[:i+1] + '()' + self.sol[i+1:]
                    backtrack(i+1)
                    self.sol = self.sol[:i+1] + self.sol[i+3:]
        
        if n>=1:
            self.sol = "()"
            backtrack(0)

        return res