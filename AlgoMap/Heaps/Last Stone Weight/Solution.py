class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        maxHeap = [-x for x in stones]

        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:

            y = -heapq.heappop(maxHeap) 
            x = -heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap,x-y)
        
        
        
        return -heapq.heappop(maxHeap) if len(maxHeap) == 1 else  0
        
        