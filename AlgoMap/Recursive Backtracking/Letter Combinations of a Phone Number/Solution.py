class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
            
        res = []
        self.sol = ""
        keypad = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}

        def backtrack(i):

            if i == len(digits):
                res.append(self.sol)
                return 
            
            for ch in keypad[int(digits[i])]:
                self.sol = self.sol + ch
                backtrack(i+1)
                self.sol = self.sol[:len(self.sol)-1]
        
        backtrack(0)
        return res

