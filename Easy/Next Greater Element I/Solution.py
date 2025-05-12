class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        next_gre = {}
        stack = []
        for num in nums2:

            while stack and stack[-1] < num:

                out = stack.pop()
                next_gre[out] = num
            
            stack.append(num)
        

        res = [-1] * len(nums1)

        for i in range(len(nums1)):
            if nums1[i] in next_gre:    
                res[i] = next_gre[nums1[i]]
        
        return res

