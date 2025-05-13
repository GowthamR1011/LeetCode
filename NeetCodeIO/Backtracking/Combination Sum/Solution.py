class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        def backtrack(sumn, ind):

            if sumn > target or ind == len(nums):
                return 
            
            if sumn == target:
                res.append(sol[:])
                return 
            

            
            sol.append(nums[ind])
            backtrack(sumn + nums[ind], ind)
            sol.pop()
            backtrack(sumn, ind + 1)
        
        backtrack(0,0)
        return res