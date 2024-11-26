from collections import deque
class Solution:
    def getExits(self,maze:List[List[str]]) -> List[List[int]]:
        exits = []
        n = len(maze[0])
        m = len(maze)
        for i in range(m):
            if maze[i][0] == '.':
                exits.append([i,0])
            if maze[i][n-1] == '.':
                exits.append([i,n-1])
        
        for j in range(1,n-1):
            if maze[0][j] == '.':
                exits.append([0,j])
            
            if maze[m-1][j] == '.':
                exits.append([m-1,j])

        
        return exits

    def getNeighbours(self,maze,i,j):
        neighbours = []
        if i > 0 and maze[i-1][j] == '.':  #Move UP
            neighbours.append([i-1,j])
        
        if i < len(maze) - 1 and maze[i+1][j] == '.': # Move Down
            neighbours.append([i+1,j])
        
        if j > 0 and maze[i][j-1] == '.': # Move left
            neighbours.append([i,j-1])
        
        if j < len(maze[0]) - 1 and maze[i][j+1] == '.':
            neighbours.append([i,j+1])
        

        return neighbours

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

       
        m,n = len(maze),len(maze[0])
        entrance_row,entrance_column = entrance
        directions = [(-1,0),(1,0),(0,-1),(0,1)]


        exits = self.getExits(maze)
        
        if entrance in exits:
            exits.remove(entrance)
        
        if len(exits) == 0:
            return -1 
        
 



        #Initialize Length Matrix and Queue
        # min_length = [[-1] * n) for _ in range(m)]
        queue = deque()


        #Setting Entrance Values
        queue.append((entrance_row,entrance_column,0))
        # min_length[entrance[0]][entrance[1]] = 0



        # print(min_length)

        while queue:

            # print(min_length)
            i,j,dist = queue.popleft() #get current position

            # current_neighbours = self.getNeighbours(maze,i,j)
            # print(current_neighbours)



            for d in directions:
                
                x = i + d[0]
                y = j + d[1]

                if [x,y] in exits:
                    
                    return dist + 1
                
                if  0 <= x < m and 0 <= y < n and maze[x][y] == '.':
                    # min_length[neighbour[0]][neighbour[1]] = min_length[i][j] + 1

                    maze[x][y] = '+'
                    queue.append((x,y,dist+1))

                

      
        return -1 