class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        grid = [[1 for _ in range(n)] for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        return grid[m-1][n-1]

        ## Memoization Technique
        # memo = {}
        # def checkMN(m,n):
        #     if m == 1 or n == 1:
        #         return 1
        #     if (m,n) in memo:
        #         return memo[(m,n)]
            
        #     memo[(m,n)] = checkMN(m-1,n) + checkMN(m,n-1)
        #     return memo[(m,n)]

        # return checkMN(m,n)
        