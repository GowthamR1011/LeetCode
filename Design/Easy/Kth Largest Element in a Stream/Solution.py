class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums[:]
        self.k = k
        heapify(self.minHeap)


        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)



    def add(self, val: int) -> int:
        
        if not self.minHeap or len(self.minHeap) < self.k:
            heapq.heappush(self.minHeap,val)
        
        elif self.minHeap[0] < val:
            heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, val)
        
        return self.minHeap[0] if len(self.minHeap) == self.k else -1



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)