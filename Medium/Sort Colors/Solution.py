class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p,q = 0,len(nums) - 1
        curr = 0


        while curr <= q:

            if nums[curr] == 0:
                nums[curr], nums[p] = nums[p], nums[curr]

                p += 1
                curr += 1
            
            elif nums[curr] == 2:
                nums[curr], nums[q] = nums[q], nums[curr]
                q -= 1
            
            else:
                curr += 1
        
    
        