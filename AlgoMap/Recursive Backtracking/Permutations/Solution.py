class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        sol,res = [],[]

        def backtrack():

            if len(sol) == len(nums):
                res.append(sol[:])
                return
            

            for x in nums:
                if x not in sol:
                    # print(x)
                    sol.append(x)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
