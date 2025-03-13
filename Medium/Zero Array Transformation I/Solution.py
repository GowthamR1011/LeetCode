class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        
        n = len(nums)
        pre_sum = [0] * n
        
        for [l,r] in queries:

            pre_sum[l] -= 1
            if r+1< n:
                pre_sum[r+1] +=1
        

        prev = 0
        for i in range(n):
            
            pre_sum[i] += prev
            if nums[i] + pre_sum[i] > 0:
                return False

            prev = pre_sum[i]

        
        return True
            