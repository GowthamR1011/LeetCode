class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res,sol = [],[]

        def backtrack(i):
            if sum(sol) > target:
                return
            
            if sum(sol) == target:
                res.append(sol[:])
                return 
            
            for index in range(i,len(candidates)):
                sol.append(candidates[index])
                backtrack(index)
                sol.pop()
        

        backtrack(0)
        return res
