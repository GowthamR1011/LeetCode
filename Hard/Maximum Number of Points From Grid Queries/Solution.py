class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        mv = [[1,0],[0,1],[-1,0],[0,-1]]
        m,n,k = len(grid), len(grid[0]), len(queries)
        res = [0] * k
        pts, curr = 0,0

        q = [(val,i) for i,val in enumerate(queries)]
        q.sort()

        minHeap = [(grid[0][0],0,0)]
        heapify(minHeap)

        seen = set([(0,0)])

        
        for limit, idx in q:
            while minHeap and minHeap[0][0] < limit:
                
                _, x,y = heappop(minHeap)
                
                pts += 1
                for u,v in mv:
                    if 0<=x+u<m and 0<=y+v<n and (x+u,y+v) not in seen:
                        heappush(minHeap,(grid[x+u][y+v],x+u,y+v))
                        seen.add((x+u,y+v))

            res[idx] = pts
        return res

