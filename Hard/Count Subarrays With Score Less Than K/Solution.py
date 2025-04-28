class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        n = len(nums)
        res = 0
        sumn = 0
        l, r =0,0
        while r < n:
            
            sumn += nums[r]

            while l <= r and sumn * (r - l + 1) >= k:
                sumn -= nums[l]
                l += 1
            
            res += r - l + 1
            r += 1

        return res