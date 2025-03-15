class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def isPossible(target):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= target:
                    count += 1
                    i += 1
                    if count == k:
                        return True

                i += 1
            return False
        
        l, r = min(nums),max(nums)

        while l <= r:
            target = (l+r) // 2
            
            if isPossible(target):
                r = target -1
            else:
                l = target + 1
            
        
        return l
        
            


            

