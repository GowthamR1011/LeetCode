class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        counts = [0] * (4*9)
        maxm = 0
        dp = {0:0}
        for i in range(1,n+1):

            q = i // 10
            d = i % 10

            dp[i] = d + dp[q]

            counts[dp[i]-1] += 1
            maxm = max(maxm,counts[dp[i]-1])
        
        
        return counts.count(maxm)