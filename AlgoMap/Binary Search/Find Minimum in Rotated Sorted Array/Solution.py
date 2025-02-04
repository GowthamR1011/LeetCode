class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums) - 1
        result = 0
        while nums[low]>nums[high]:
            
            mid = (low+high) // 2

            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid]  > nums[low]:
                low = mid+1
            else:
                high = mid - 1
                

        return nums[low]