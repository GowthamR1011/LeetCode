class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        

        nums = sorted([[nums2[i], nums1[i]] for i in range(len(nums1))], key = itemgetter(0), reverse = True)

        sumn= 0
        res = 0
        minm = []
        heapify(minm)
        for a , b in nums:
            sumn += b
            heappush(minm,b)

            if len(minm) == k:
                res = max(res,sumn * a)
                sumn -= heappop(minm)
        
        return res

             