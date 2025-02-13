class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    stack = [(i,j)]
                    area = 0

                    while stack:

                        p,q = stack.pop()
                        
                        if 0<=p<m and 0<=q<n and grid[p][q] == 1:
                            area += 1
                            grid[p][q] = 2

                            stack.append((p-1,q))
                            stack.append((p,q-1))
                            stack.append((p+1,q))
                            stack.append((p,q+1))
                    
                    maxArea = max(area,maxArea)
        
        return maxArea