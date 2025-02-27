class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp=[[ 2 for _ in range(n)] for _ in range(n)]
        res = 0
        valToidx = {}
        for idx,val in enumerate(arr):
            valToidx[val] = idx
        for i in range(2,n):
            for j in range(i):
                diff = arr[i] -  arr[j]
                if diff in valToidx  and valToidx[diff] < j:
                    dp[i][j] = dp[j][valToidx[diff]] + 1,

                res = max(res,dp[i][j])
        
        return res if res > 2 else 0
