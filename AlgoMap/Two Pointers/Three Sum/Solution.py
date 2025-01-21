
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for i in range(len(nums)-2):
            if(i > 0 and nums[i] == nums[i-1]):
                continue

            left = i+1
            right = len(nums) - 1
            sum_value = -1 * nums[i]

            while left<right:

                if(nums[left]+nums[right] == sum_value):
                    result.append([nums[left],nums[i],nums[right]])
                    right -=1
                    left +=1 
                    while nums[left]== nums[left-1] and left<right:
                        left +=1
                    while nums[right] == nums[right+1] and left<right:
                        right -=1
                elif sum_value <= nums[left]+nums[right]:
                    right -=1
                else:
                    left +=1
            
            
        
        return result
            
                
                
