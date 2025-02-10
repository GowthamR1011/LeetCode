class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        maxHeap = [-x for x in nums]

        heapq.heapify(maxHeap) # Heapify has a Time: O(n) better than sorting. 

        for _ in range(k):
            maxm = -heapq.heappop(maxHeap)
        
        return maxm