class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0 
        high = len(nums) - 1
        result = -1 
        while nums[low]>nums[high]:
            
            mid = (low+high) // 2

            if nums[mid] > nums[mid+1]:
                result = mid+1
                break
                
            if nums[mid-1] > nums[mid]:
                result = mid
                break
            if nums[mid]  > nums[low]:
                low = mid+1
            else:
                high = mid - 1
        print(result)
        if result == -1:
            low = 0
            high = len(nums) - 1
        
        elif nums[len(nums)-1] >= target:
            low = result 
            high = len(nums) - 1
        else:
            low = 0
            high = result - 1
        
        while low<=high:
            mid = (low+high) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return -1