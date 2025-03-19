class Solution:
    def minOperations(self, nums: List[int]) -> int:
 
        count = 0
        
        for l in range(len(nums)-2):

            if nums[l] == 0:
                count += 1
                nums[l] = 1
                nums[l+1] = abs(nums[l+1] - 1)
                nums[l+2] = abs(nums[l+2]-1)


        return count if nums[-2] and nums[-1] else -1