class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        
        def isZero(n,k):

            lines = []
            pre_sum = [0] * n

            for [l,r,val] in queries[:k]:

                pre_sum[l] -= val
                if r < n-1:
                    pre_sum[r+1] += val

            prev = 0
            for i in range(n):

                pre_sum[i] += prev

                if pre_sum[i] + nums[i] > 0:
                    return False

                prev = pre_sum[i]
            
            return True
        
        n= len(nums)
        q = len(queries)
        low,high = 0,q
        res = -1

        while low<=high:

            mid = (low + high) // 2

            if isZero(n,mid):
                res = mid
                high = mid-1
            else:
                low = mid+1


        return res



        