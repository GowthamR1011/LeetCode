class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        dp = [[0] * (2) for _ in range(n+1)]

        for i in range(n-1,-1,-1):
            for j in range(2):

                buy, sell = -1e9, -1e9

                if not j:
                    buy =  dp[i+1][1] - prices[i]
                else:
                    sell = prices[i] - fee + dp[i+1][0]
                
                moveon = dp[i+1][j]

                dp[i][j] = max(sell,buy,moveon)
         
        return dp[0][0]