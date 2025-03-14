class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        s = sum(nums[:k])
        maxm = s
        
        for i in range(k,len(nums)):

            s += nums[i] - nums[i-k]
            maxm = max(s,maxm)
        

        return maxm/k

