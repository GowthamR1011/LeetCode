class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        minHeap = []
        heapify(minHeap)
        included = [False] * len(nums)

        for i in range(k):
            included[i] = True
            heappush(minHeap,(nums[i],i))
        
        for i in range(k,len(nums)):

            if nums[i] > minHeap[0][0]:
                _,idx = heappop(minHeap)
                included[idx] = False
                included[i] = True
                heappush(minHeap,(nums[i],i))
        
        res = []

        for i in range(len(nums)):
            if included[i]:
                res.append(nums[i])
        
        
        return res
        


        

        
            