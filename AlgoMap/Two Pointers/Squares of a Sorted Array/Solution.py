class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
        
        

        left = i - 1
        right = i
        result = []
        while left >= 0 and right < len(nums):

            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[left]**2)
                left -= 1
            else:
                result.append(nums[right]**2)
                right += 1
            
        while left>=0:
            result.append(nums[left]**2)
            left -=1
        
        while right<len(nums):
            result.append(nums[right]**2)
            right += 1
        
        return result
