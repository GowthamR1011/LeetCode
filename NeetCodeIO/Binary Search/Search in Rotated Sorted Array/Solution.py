class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        l, h = 0, len(nums) - 1


        while l < h:

            m = (l + h) // 2

            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
        

        crux = l
        if crux == 0:
            l = 0
            h = len(nums) - 1

        elif nums[0] <= target <= nums[crux-1]:
            l = 0
            h = crux - 1
        else:
            l = crux
            h = len(nums) - 1
        

        while l<=h:
            m = (l+h) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                h = m - 1
            else:
                l = m + 1
        
        return -1

            