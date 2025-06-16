class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        
        if not nums:
            return -1
        
        minm = nums[0]
        maxm = 0

        for num in nums[1:]:

            maxm = max(num - minm, maxm)
            minm = min(minm, num)
        

        return maxm if maxm > 0 else -1