class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        
        if len(nums) == 0:
            return 0

        nums.sort()
        res = 1
        minm =  nums[0]

        for num in nums[1:]:

            if num - minm > k:
                res += 1
                minm = num
        
        return res
