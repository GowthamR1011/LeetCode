class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n


        digits = 1 
        count = 9
        while n > digits * count:
            n -= digits * count
            
            digits += 1
            count *= 10

        start = 10**(digits-1)
        num = start + ((n-1)//digits)
        rem = n % digits
        
        return int(str(num)[rem-1])
