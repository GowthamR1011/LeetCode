class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [inf] * (amount+1)
        dp[0] = 0
        coins.sort()

        for i in range(1,amount+1):
            for x in coins:
                if x > i:
                    break
                else:
                    dp[i] = min(dp[i],1+dp[i-x])
        
        if dp[amount] < inf:
            return dp[amount]
        
        return -1