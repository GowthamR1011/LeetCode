class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_w = 0
        l,r= 0,0 
        n_zeros = 0
        while r<len(nums):
            if nums[r]==0:
                n_zeros += 1
            if n_zeros > k:
                if nums[l] == 0:
                    n_zeros -= 1
                l += 1

            max_w = max(max_w,r-l+1)
            r += 1
        return max_w
            

        return -1  
