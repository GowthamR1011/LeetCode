class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        l,r,res = 0,1,1

        xor = nums[l]

        while r < len(nums):

            if xor ^ nums[r] == xor + nums[r]:
                xor = xor ^ nums[r]
                print(xor)
                res = max(res, r - l + 1)

            
            else:
                while xor ^ nums[r] != xor + nums[r] and l < r:
                    xor = xor ^ nums[l]

                    l += 1
                xor = xor ^ nums[r]
            r += 1

        return res



