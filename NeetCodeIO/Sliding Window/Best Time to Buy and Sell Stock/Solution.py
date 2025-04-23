class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = 101
        res = 0

        for price in prices:

            low = min(price,low)
            res = max(res, price-low)
        
        return res