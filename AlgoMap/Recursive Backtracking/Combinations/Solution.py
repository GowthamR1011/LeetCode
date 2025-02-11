class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res,sol = [],[]

        def backtrack(i):

            if len(sol) == k:
                res.append(sol[:])
                return 
                

            for index in range(i,n+1):
                sol.append(index)
                backtrack(index+1)
                sol.pop()
    
        backtrack(1)
        return res