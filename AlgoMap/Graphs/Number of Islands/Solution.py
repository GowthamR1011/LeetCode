class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island += 1
                    stack = [(i,j)]
                    while stack:
                        p,q = stack.pop()
                        if 0<= p < len(grid) and 0<=q < len(grid[0]) and grid[p][q] == '1':
                            grid[p][q] = '*'
                            stack.append((p-1,q))
                            stack.append((p,q-1))
                            stack.append((p+1,q))
                            stack.append((p,q+1))
                    
        
        return island

