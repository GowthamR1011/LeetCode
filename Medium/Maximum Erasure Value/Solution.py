class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0

        seen = set()
        sumn = 0
        res = 0

        for num in nums:
            
            while num in seen:
                seen.remove(nums[l])
                sumn -= nums[l]
                l += 1
                

            seen.add(num)
            sumn += num

            res = max(res,sumn)
        
        return res


                