class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        res = 1 
        div = n < 0 
        n = -n if div else n

        while n > 0:
            if n & 1:
                if div:
                    res = res / x
                else:
                    res = res * x
            
            x = x * x
            n >>= 1

        return res