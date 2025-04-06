import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)

        while low<=high:
            mid = (low+high) // 2
            time = sum([ceil(x/mid) for x in piles])

            if time > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low


            