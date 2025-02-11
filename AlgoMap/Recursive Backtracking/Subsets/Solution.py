class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sol = []

        def backtrack(index):

            if index == len(nums):
                res.append(sol[:])
                return
            

            backtrack(index+1)


            sol.append(nums[index])
            backtrack(index+1)
            sol.pop()
        
        backtrack(0)
        return res

