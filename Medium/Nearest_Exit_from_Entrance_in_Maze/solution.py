from collections import deque
class Solution:
    


    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

       
        #Initialize the Variables
        m,n = len(maze),len(maze[0])
        entrance_row,entrance_column = entrance
        directions = [(-1,0),(1,0),(0,-1),(0,1)]


        queue = deque()


        #Setting Entrance Values
        queue.append((entrance_row,entrance_column,0))
        maze[entrance_row][entrance_column] = '+'
        





        while queue:

            i,j,dist = queue.popleft() #get current position and distance

            for d in directions:
                
                x,y = i + d[0],j + d[1]   # Getting the neighbour points 
                
                if  0 <= x < m and 0 <= y < n and maze[x][y] == '.': # Check if neighbour points are valid and not a wall
                    if x == 0 or x == m-1 or y == 0 or y == n-1: # Check if the neighbour point is an exit
                        return dist + 1

                    maze[x][y] = '+' # If not an exit, we mark the neighbour as visited (with making it wall)
                    queue.append((x,y,dist+1)) # Now adding it to the queue to be tranversed later

                

      
        return -1 # If the queue ends with no more traversals, it means no exit can be reached. 