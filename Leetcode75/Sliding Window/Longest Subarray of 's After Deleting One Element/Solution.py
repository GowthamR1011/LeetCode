class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        l,r,count,maxm = 0,0,0,0

        while r<len(nums):
            if nums[r] == 0:
                count += 1
            
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            
            maxm = max(maxm,r - l)
            r += 1

        return maxm


