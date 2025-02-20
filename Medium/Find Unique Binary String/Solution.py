class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        s = set([int(x,2) for x in nums])
        n = len(nums[0])
        for i in range(0,2**(n)):
            if i not in s:
                return bin(i)[2:].zfill(n)
        
        