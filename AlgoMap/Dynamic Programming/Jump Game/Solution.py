class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        curr = nums[0]
        
        for i in nums[:n-1]:
            
            curr -= 1
            curr = max(i,curr)
            if curr == 0:
                return False

        return True 