class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        mi = abs(nums[0])
        x = nums[0]
        for i in nums:
            if abs(i) < mi or (abs(i) == mi and x < i ):
                x = i
                mi = abs(i)

        
        return x
