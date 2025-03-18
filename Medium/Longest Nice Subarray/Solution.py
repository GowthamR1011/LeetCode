class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        l,r,res = 0,1,1

        xor = nums[l]

        while r < len(nums):
            while xor ^ nums[r] != xor + nums[r] and l < r:
                xor = xor ^ nums[l]
                l += 1
            
            xor = xor ^ nums[r]
            res = max(res, r - l + 1)    
            r += 1

        return res



