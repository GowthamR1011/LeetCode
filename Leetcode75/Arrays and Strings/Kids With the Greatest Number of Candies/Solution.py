class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxm = max(candies)
        res = []
        for candy in candies:

            if candy + extraCandies >=maxm:
                res.append(True)

            else:
                res.append(False)
        
        return res