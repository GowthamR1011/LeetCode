class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        count_zero_1 = nums1.count(0)
        count_zero_2 = nums2.count(0)

        min_sum_1 = sum(nums1) + count_zero_1
        

        min_sum_2 = sum(nums2) + count_zero_2
        

        if count_zero_1 == 0 and min_sum_1 < min_sum_2:
            return -1
        
        if count_zero_2 == 0 and min_sum_2 < min_sum_1:
            return -1
        


        return max(min_sum_1 , min_sum_2)
