class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        
        n = len(nums) // 3
        minDp = [inf] * ( 3 * n)
        maxDp = [-inf] * (3 * n)

        maxHeap = [-v for v in nums[:n]]
        heapify(maxHeap) 

        minDp[n-1] =-1 * sum(maxHeap)
        

        for i in range(n,3*n):
            if nums[i] < -maxHeap[0]:
                val = -heappop(maxHeap)
                heappush(maxHeap,-nums[i])
                minDp[i] = minDp[i-1] + nums[i] - val
            else:
                minDp[i] = minDp[i-1]
        


        minHeap = [v for v in nums[2*n:]]
        heapify(minHeap)

        maxDp[2*n] = sum(minHeap)
        for i in range(2*n - 1, -1, -1):
            if nums[i] > minHeap[0]:
                val = heappop(minHeap)
                heappush(minHeap,nums[i])
                maxDp[i] = maxDp[i+1] + nums[i] - val
            else:
                maxDp[i] = maxDp[i+1]
        

        res = inf
        for i in range(n-1, 2*n ):
            res = min(res, minDp[i] - maxDp[i+1])



        return res
            




                

            


