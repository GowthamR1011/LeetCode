class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        diff, res, hi = 0 , 0, 0

        for num in nums:
            res = max(res,diff * num)
            diff = max(diff, hi - num)
            hi = max(hi,num)

        return res