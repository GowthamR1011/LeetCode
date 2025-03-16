class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def isPossible(t):

            count = 0
            for r in ranks:
                count += int(sqrt(t/r))
                if count >= cars:
                    return True
            
            return False
        
        l ,r, res =1, min(ranks) * cars**2, min(ranks) * cars**2 


        while l <= r:

            mid = (l+r) // 2

            if isPossible(mid):
                r = mid - 1
                res = min(mid,res)
            else:
                l = mid + 1
        
        return res