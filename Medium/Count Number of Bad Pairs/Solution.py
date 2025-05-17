class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        res = 0
        count_map = defaultdict(int)

        for i in range(n):
            res += i - count_map[nums[i] - i]     
            count_map[nums[i] - i] += 1   
        
        return res
