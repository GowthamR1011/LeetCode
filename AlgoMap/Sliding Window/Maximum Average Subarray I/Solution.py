class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    
        s = sum(nums[:k])
        max_sum = s
        for i in range(k,len(nums)):
            s += nums[i] -nums[i-k]
            max_sum = max(s,max_sum)
            
        return max_sum/k
            
