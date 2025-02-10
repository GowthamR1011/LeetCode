class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distance = []

        for i in range(len(points)):
            d = sqrt(points[i][0] **2 + points[i][1]** 2)
            distance.append((d,i))

        heapq.heapify(distance)
        result = []

        for _ in range(k):
            min_d = heapq.heappop(distance)
            result.append(points[min_d[1]])
        
        return result