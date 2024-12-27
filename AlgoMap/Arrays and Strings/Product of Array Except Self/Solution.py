class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [1 for _ in range(n)],[1 for _ in range(n)]
        for i in range(1,n):
            left[i] = left[i-1] * nums[i-1]
            right[n-i-1] = right[n-i] * nums[n-i]
        
        return [left[i]* right[i] for i in range(n)]
        
        
