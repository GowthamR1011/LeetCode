class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l,r = 0,0
        min_length = inf
        s = 0
        while r<len(nums):
            s+= nums[r]
            while s >=target:
                min_length = min(min_length,r-l+1)
                s -= nums[l]
                l = l+1
            
  
            r = r+1
        
        if min_length == inf:
            return 0
        return min_length

            