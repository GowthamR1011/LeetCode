class Solution:

    def __init__(self, nums: List[int]):        
        self.nums = nums
        
    def pick(self, target: int) -> int:
        if len(self.nums) ==1:
            return 0
        
        while True:
            i = randint(0,len(self.nums)-1)
            if self.nums[i] == target: 
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)