class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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