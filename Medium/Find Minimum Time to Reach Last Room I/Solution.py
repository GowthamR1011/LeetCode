class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        
        n,m = len(moveTime), len(moveTime[0])

        min_heap = [(0,0,0)] # t,i,j
        heapify(min_heap)

        direc = [(1,0),(0,1),(0,-1),(-1,0)]
        min_times = {}
        
        while min_heap:

            t, r, c = heappop(min_heap)

            if (r,c) in min_times:
                continue
            
            min_times[(r,c)] = t

            for x,y in direc:
                i = r + x
                j = c + y

                if 0<=i<n and 0<=j<m:

                    heappush(min_heap,(max(t+1,moveTime[i][j] + 1),i,j))
        

        return min_times[(n-1,m-1)] 