class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        count = 0
        res = 0
        count_map = {0:-1}
        for i in range(len(nums)):

            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            
            if count in count_map:
                res = max(res, i - count_map[count])
            else:
                count_map[count] = i
        
        return res