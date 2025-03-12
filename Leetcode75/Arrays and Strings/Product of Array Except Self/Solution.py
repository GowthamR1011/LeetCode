class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        left = 1
        right = n-2

        left_prod = [1] * n
        right_prod = [1] * n 
        while left < n:

            left_prod[left] = left_prod[left-1] * nums[left-1]
            right_prod[right] = right_prod[right+1] * nums[right+1]
        
            left +=1 
            right -= 1
        
        return [left_prod[i] * right_prod[i] for i in range(n)]


        
        
