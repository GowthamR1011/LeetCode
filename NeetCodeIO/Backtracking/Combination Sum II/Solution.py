class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        candidates.sort()

        def backtrack(sumn, i):

            if sumn == target:
                res.append(sol[:])
                return 

            if sumn > target or i >= len(candidates):
                return 
            

            sol.append(candidates[i])
            backtrack(sumn + candidates[i], i+ 1)
            sol.pop()

            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            
            backtrack(sumn, i + 1)
        
        backtrack(0,0)
        return res
        
        
