class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        c = defaultdict(int)
        res = 0
        l = 0
        n = len(nums)
        for num in nums:

            c[num] += 1

            while c[num] >= 2:
                if l <n:
                    c[nums[l]] -= 1
                if l+1< n:
                    c[nums[l+1]] -= 1
                
                if l+2 < n:
                    c[nums[l+2]] -= 1

                res += 1
                l += 3

        return res