class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)

        p2 = [1]

        for x in range(n):
            p2.append(p2[-1] * 2 % MOD)

        l,r = 0, n - 1

        res = 0 
        while l <= r and nums[l] <= target:

            while r >= 0 and nums[l] + nums[r] > target:
                r -= 1
            
            if r < l:
                break

            res+= p2[r-l]
        
            l += 1
        
        return res % MOD
