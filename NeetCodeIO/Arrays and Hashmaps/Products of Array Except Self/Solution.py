class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        left_pro = [1] * n
        right_pro = [1] * n
        for i in range(1,n-1):
            left_pro[i] = left_pro[i-1] * nums[i-1]
            right_pro[n-i-1] = right_pro[n-i] * nums[n-i]

        left_pro[n-1] = left_pro[n-2] * nums[n-2]
        right_pro[0] = right_pro[1] * nums[1]
        

        return [left_pro[i] * right_pro[i] for i in range(n)]

