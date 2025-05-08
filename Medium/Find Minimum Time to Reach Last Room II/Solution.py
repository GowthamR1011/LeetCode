class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n,m = len(moveTime), len(moveTime[0])


        min_heap = [(0,0,0,True)] # t,i,j,odd_step
        heapify(min_heap)

        direc = [(1,0),(0,1),(0,-1),(-1,0)]
        min_times = [[inf for _ in range(m)] for _ in range(n)]
        
        while min_heap:

            t, r, c, odd_step = heappop(min_heap)
            
            if r == n-1 and c == m -1:
                return t

            for x,y in direc:
                i = r + x
                j = c + y

                if 0<=i<n and 0<=j<m:
                    new_time = max(t,moveTime[i][j]) + 1
                    if not odd_step:
                        new_time += 1
                    
                    if new_time < min_times[i][j]:
                        min_times[i][j] = new_time
                        heappush(min_heap,(new_time,i,j,not odd_step))
        

        return min_times[n-1][m-1] 