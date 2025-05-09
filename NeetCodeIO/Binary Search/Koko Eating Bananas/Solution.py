class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)

        while low<=high:

            m = (low + high) // 2

            tt = sum([math.ceil(p/m) for p in piles])

            if tt > h:
                low = m + 1
            else:
                high = m -  1
        

        return low
            
