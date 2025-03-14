class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        s = sum(nums)
        prev = 0

        for i in range(len(nums)):
            
            if prev == s - nums[i] - prev:
                return i

            prev += nums[i]
        
        return -1
        
