class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        maxB = nums[0]

        for num in nums[1:]:
            maxB = maxB | num
        


        memo = [[-1] * (maxB + 1) for _ in range(len(nums))]
        def backtrack(i, curr, maxB):

            if i == len(nums):
                return 1 if curr == maxB else 0
            
            if memo[i][curr] != -1:
                return memo[i][curr]

            
            memo[i][curr] = backtrack(i+ 1, curr, maxB) + backtrack(i+1,curr | nums[i], maxB)

            return memo[i][curr]
        


        return backtrack(0,0,maxB)
        
