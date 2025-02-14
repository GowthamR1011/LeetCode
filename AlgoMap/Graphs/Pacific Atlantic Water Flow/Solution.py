class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        m = len(heights)
        n = len(heights[0])

        movements = [[1,0],[0,1],[0,-1],[-1,0]]
        stack_p = []
        stack_a = []

        atlantic_check_grid = [[0 for _ in range(n)] for _ in range(m)]
        pacific_check_grid = [[0 for _ in range(n)] for _ in range(m)]

        
        for i in range(m):
            atlantic_check_grid[i][n-1] = 2
            stack_a.append([i,n-1])

            pacific_check_grid[i][0] = 2
            stack_p.append([i,0])

        for j in range(n):
            atlantic_check_grid[m-1][j] = 2
            stack_a.append([m-1,j])

            pacific_check_grid[0][j] = 2
            stack_p.append([0,j])
         

        while stack_a:

            p,q = stack_a.pop()

            for x,y in movements:

                if 0<=p+x<m and 0<=q+y < n and heights[p+x][q+y] >= heights[p][q] and atlantic_check_grid[p+x][q+y] != 2:
                    stack_a.append([p+x,q+y])
                    atlantic_check_grid[p+x][q+y] = 2

        while stack_p :

            p,q = stack_p.pop()

            for x,y in movements:
                if 0<=p+x<m and 0<=q+y < n and heights[p+x][q+y] >= heights[p][q] and pacific_check_grid[p+x][q+y] != 2:     
                    stack_p.append([p+x,q+y])
                    pacific_check_grid[p+x][q+y] = 2   
        

        for i in range(m):
            for j in range(n):
                if pacific_check_grid[i][j] == 2 and atlantic_check_grid[i][j] == 2:
                    res.append([i,j])

        print(pacific_check_grid)
        return res
