class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        
        
        n = len(nums)

        maxB = [-1] * 31
        res = [0] * n


        for i in range(n-1,-1,-1):

            j = i

            for bit in range(31):
                if (nums[i] &(1 << bit)) == 0:
                    if maxB[bit] != -1:
                        j = max(j,maxB[bit])
                else:
                    maxB[bit] = i
                
            
            res[i] = j - i + 1
        
        return res