class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
            
        l,h = 0, len(nums) - 1

        while l<=h:

            m = (l + h) // 2

            if m == 0 and nums[m] > nums[m+1]:
                return m
            elif m == len(nums) - 1 and nums[m] > nums[m-1]:
                return m
            
            elif nums[m] > nums[m+1] and nums[m] > nums[m-1]:
                return m 
            
            elif nums[m] < nums[m+1]:
                l = m+ 1
            else:
                h = m- 1
        
        return -1
