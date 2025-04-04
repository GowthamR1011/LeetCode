class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        potions.sort()
        
        n = len(potions) 
        m = len(spells)

        res = []
        
        for i in range(m):

            l = 0
            h = n - 1

            while l<=h:

                mid = (l+h) // 2

                if potions[mid] * spells[i] < success:
                    l = mid + 1
                else:  
                    h = mid -  1

            res.append(n - l)
        return res