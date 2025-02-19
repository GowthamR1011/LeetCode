class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cur = 0
        maxSum = -inf

        for i in nums:

            cur += i

            maxSum = max(maxSum,cur)
            cur = max(cur,0)
        
        return maxSum