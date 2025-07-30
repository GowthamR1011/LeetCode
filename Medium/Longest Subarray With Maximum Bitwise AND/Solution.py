class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        maxm = max(nums)

        l , r = 0, 0
        res = 0
        while r < n:

            while nums[l] == maxm and r < n - 1 and (nums[r+1] == nums[l]):
                r += 1
            
            res = max(res,r - l + 1)
            r += 1
            l = r
        

        return res
