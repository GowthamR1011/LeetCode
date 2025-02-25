class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
       
        res = 0
        odd_sum = 0
        even_sum = 0
        pre_sum = 0
        for i in range(len(arr)):
        
            pre_sum += arr[i]
            if pre_sum % 2 == 1:
                res += (i-odd_sum) + 1
                odd_sum += 1
                
            else:
                res += (i - even_sum) 
                even_sum += 1   
                     
        
        return res % (10**9 + 7)  