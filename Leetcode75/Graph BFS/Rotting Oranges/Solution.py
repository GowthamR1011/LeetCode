class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mv = [(-1,0),(0,-1),(0,1),(1,0)]

        fresh = 0
        q = deque([])
        m , n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j,0))
        
        if fresh == 0:
            return 0
        
        while q:

            x,y,t = q.popleft()
            for i,j in mv:
                if 0<=x+i<m and 0<=y+j<n and grid[x+i][y+j] == 1:
                    grid[x+i][y+j] = 2
                    q.append((x+i,y+j,t+1))
                    fresh -= 1

                    if fresh == 0:
                        return t+1
        
        return -1
        
