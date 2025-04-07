class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        if len(digits) == 0:
            return []
        phone = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}

        curr, res = [],[]
        def backtrack(i):

            if i == len(digits):
                res.append("".join(curr))
                return
            
            for ch in phone[int(digits[i])]:
                curr.append(ch)
                backtrack(i+1)
                curr.pop()
        
        backtrack(0)
        return res