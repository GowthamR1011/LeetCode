class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        
        num_zeros = 0

        n = len(nums)
        i=0
        while i<n:
            if nums[i] > 0:
                break
            elif nums[i] == 0:
                num_zeros += 1
        
            i += 1

        return max(n-i,i - num_zeros)