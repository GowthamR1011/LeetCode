class Solution:
    
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def firstPositive(nums):

            l,r = 0, len(nums)

            while l < r:

                m = (l + r) // 2

                if nums[m] >= 0:
                    r = m
                else:
                    l = m + 1
            
            return r
        


        n1, n2 = len(nums1), len(nums2)

        p = firstPositive(nums1)
        q = firstPositive(nums2)

        l,r = int(-1e10), int(1e10)

        while l <=r :

            m = (l + r) // 2

            count = 0

            i, j = 0, q - 1

            while i < p and j >= 0:

                if nums1[i] * nums2[j] > m:
                    i += 1
                
                else:
                    count += p - i
                    j -= 1
            
            i, j = p,  n2 - 1
            while i < n1 and j >= q:
                if nums1[i] * nums2[j] > m:
                    j -= 1
                else:
                    count += j - q + 1
                    i += 1
            
            i, j = 0, q
            while i < p and j < n2:
                if nums1[i] * nums2[j] > m:
                    j += 1
                else:
                    count += n2 - j
                    i += 1
            
            i, j = p, 0
            while i < n1 and j < q:
                if nums1[i] * nums2[j] > m:
                    i += 1
                else:
                    count += n1 - i
                    j += 1
            
            if count < k:
                l = m + 1
            else:
                r = m - 1
        
        return l



        
                

        

