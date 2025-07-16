class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        odds = evens = count = 0
        
        prev = 1 - nums[0] % 2

        for i in range(len(nums)):
            if nums[i] & 1 :
                odds += 1
            else:
                evens += 1
            
            if nums[i] % 2 != prev:
                count += 1
                prev = 1 - prev
        

        return max(count,odds,evens)