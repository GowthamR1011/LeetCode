class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        xors = []

        res = 0
        def backtrack(curr, i):

            if i == len(nums):
                xors.append(curr)
                return 
            
            temp = curr
            curr ^= nums[i]

            backtrack(curr,i+1)
            backtrack(temp,i+1)
        
        backtrack(0,0)


        return sum(xors)



        
