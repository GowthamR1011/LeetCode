class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left,right, count, maxm = 0,0,0,0

        while right < len(nums):

            if nums[right] == 0:
                count += 1
        
            while count > k:
            
                if nums[left] == 0:
                    count -=1 
            
                left += 1

            maxm = max(maxm, right - left + 1)

            right += 1
            
        return maxm