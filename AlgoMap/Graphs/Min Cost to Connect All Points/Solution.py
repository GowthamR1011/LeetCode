class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        distHeap = [(0,0)]
        seen = set()
        cost,edges  = 0,-1

        heapq.heapify(distHeap)

        while edges < len(points)-1:
            d,i = heapq.heappop(distHeap)

            if i not in seen:

                seen.add(i)
                cost += d
                edges += 1

                for j in range(len(points)):
                    if j not in seen:
                        heapq.heappush(distHeap,(abs(points[i][0]- points[j][0]) + abs(points[i][1]-points[j][1]),j))
        
        return cost