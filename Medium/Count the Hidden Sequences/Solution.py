class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        res = 0
        minm,maxm = 0,0

        for d in differences:
            res +=  d
            minm = min(minm,res)
            maxm = max(maxm,res)
            
        

        return max(0, (upper - maxm) - (lower - minm) + 1)