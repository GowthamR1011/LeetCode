class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        maxHeap = []
        for key in counter:
            heapq.heappush(maxHeap,(-counter[key],key))
        
        result = []

        for _ in range(k):

            result.append(heapq.heappop(maxHeap)[1])
        
        return result