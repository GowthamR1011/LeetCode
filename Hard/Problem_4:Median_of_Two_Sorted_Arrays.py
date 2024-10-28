'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)). '''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1 = 0 
        l2 = 0

        new_list = []
        while l1 < len(nums1) and l2 < len(nums2):
            if nums1[l1] <nums2[l2]:
                new_list.append(nums1[l1])
                l1 += 1
            else:
                new_list.append(nums2[l2])
                l2 += 1
            
        while l1<len(nums1):
            new_list.append(nums1[l1])
            l1 += 1
        
        while l2<len(nums2):
            new_list.append(nums2[l2])
            l2 += 1
        
        print(new_list)
        if len(new_list) % 2 != 0:
            return new_list[len(new_list)//2]
     
     
        return (new_list[len(new_list)//2-1] + new_list[len(new_list)//2]) / 2