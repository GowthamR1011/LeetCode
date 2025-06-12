class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        
        maxm = abs(nums[0] - nums[-1])

        for i in range(1,len(nums)):
            maxm= max(maxm, abs(nums[i] - nums[i-1]))
        
        return maxm