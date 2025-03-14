class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        max_candies,min_candies = sum(candies)//k,1

        def isPossible(x):
      
            count = 0
            for num in candies:
                count += num // x
        
            return count >= k
        
        res = 0
        while min_candies <= max_candies:

            mid = (min_candies + max_candies) //2 

            if isPossible(mid):
                res = mid
                min_candies = mid + 1
            else:
                max_candies = mid -1
        
        return res


            
             