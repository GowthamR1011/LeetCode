import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total_bananas = sum(piles)
        min_k = max(total_bananas // h , 1)
        max_k = max(piles) 
        
        while min_k <=max_k:
            k = (min_k + max_k) //2 
            time_taken =  sum([math.ceil(x/k) for x in piles])
            if time_taken <=h :
                max_k = k -1 
            else:
                min_k = k + 1

        return max_k + 1
            
        


            