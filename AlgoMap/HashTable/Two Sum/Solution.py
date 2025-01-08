from collections import Counter
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = Counter(nums)
        for i in range(len(nums)):
            diff = (target - nums[i])
            if  diff ==  nums[i]:
                if counter[diff] >=2 and nums.index(diff) != i:
                    return [i,nums.index(diff)]
            elif diff in counter:
                return [i,nums.index(diff)]