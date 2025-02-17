class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        seen = set({})
        adj = [[-1 for _ in range(n)] for _ in range(n)]

        for s,d,t in times:
            adj[s-1][d-1] = t

        minTime = 0
        minHeap = [(0,k-1)]
        heapq.heapify(minHeap)

        while minHeap:

            t,i = heapq.heappop(minHeap)

            if i not in seen:    
                seen.add(i)
                minTime = max(minTime,t)

                for j in range(n):
                    if adj[i][j] !=-1 and j not in seen:
                        heapq.heappush(minHeap,(minTime+adj[i][j],j))

        if len(seen) == n:
            return minTime
        
        return -1


