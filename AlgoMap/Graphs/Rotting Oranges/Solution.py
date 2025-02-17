class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        stack,curr = [],[]
        fresh_orange, minutes = 0,0


        movements = [[0,1],[1,0],[-1,0],[0,-1]]
        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_orange += 1
                elif grid[i][j] == 2:
                    curr.append((i,j))
        
        stack.append(curr[:])
        

        while stack:
            
            curr = stack.pop()
            new = []
            for x,y in curr:
                for i,j in movements:
                    if 0<=x+i<m and 0<=y+j<n and grid[x+i][y+j] == 1:
                        grid[x+i][y+j] = 2
                        new.append((x+i,y+j))
                        fresh_orange -= 1
            if len(new) > 0:
                stack.append(new[:])
                minutes+=1
        
        if fresh_orange == 0:
            return minutes
        
        return -1

