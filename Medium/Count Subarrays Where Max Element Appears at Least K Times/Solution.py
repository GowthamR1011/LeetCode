class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        maxm = max(nums)
        n = len(nums)
        res = 0

        counter = 0

        l, r = 0, 0

        while r < n:

            if nums[r] == maxm:
                counter += 1
            
            while counter >= k:
                res += (n-r) 
                if nums[l] == maxm:
                    counter -= 1
                
                l += 1

            r += 1
        
        return res