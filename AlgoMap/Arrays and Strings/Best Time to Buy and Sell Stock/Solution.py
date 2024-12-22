class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = inf
        for i in prices:
            if i < min_val:
                min_val = i
            
            if max_profit < (i - min_val):
                max_profit = i - min_val
        
        return max_profit