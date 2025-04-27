class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
    
        res = 0

        for r in range(2,n):
            if (nums[r-2] + nums[r]) == nums[r-1] / 2:
                res += 1
        
        return res