class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ind = {num:i for i,num in enumerate(nums)}

        for j in range(len(nums)):

            if target - nums[j] in ind and ind[target-nums[j]] != j:
                return [j, ind[target - nums[j]]]

        