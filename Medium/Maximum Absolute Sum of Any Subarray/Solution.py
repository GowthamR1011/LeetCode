class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        maxm = nums[0]
        sum_max = nums[0]
        sum_min = nums[0]
        minm = nums[0]
        for i in nums[1:]:

            sum_max = max(sum_max+i,i)
            maxm = max(sum_max,maxm)

            sum_min = min(sum_min+i,i)
            minm = min(sum_min,minm)
        
        return max(maxm,abs(minm))
