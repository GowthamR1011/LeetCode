class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        dp = [0] * (n+1)
        dp[n-1] = cost[-1]
        dp[n-2] = cost[-2]
        for i in range(n-3,-1,-1):

            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        return min(dp[0],dp[1])
