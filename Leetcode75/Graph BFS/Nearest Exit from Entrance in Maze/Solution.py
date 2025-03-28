class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        m , n = len(maze), len(maze[0])

        q = deque([(entrance[0],entrance[1],0)])
        mv = [(1,0),(0,1),(0,-1),(-1,0)]

        minm = inf
        maze[entrance[0]][entrance[1]] = '*'
        while q:

            x,y, steps = q.popleft()

            if (x == 0 or y == 0 or x == m-1 or y == n-1) and [x,y] != entrance:
                minm = min(steps,minm)
            

            for u,v in mv:
                if 0<= x +u <m and 0<=y+v < n and maze[x+u][y+v] == '.':
                    q.append((x+u,y+v,steps+1))
                    maze[x+u][y+v] = '*'
        return minm if minm < inf else -1
