class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = [-x for x in nums]

        heapify(max_heap)

        for i in range(k-1):
            heappop(max_heap)
        
        return -heappop(max_heap)