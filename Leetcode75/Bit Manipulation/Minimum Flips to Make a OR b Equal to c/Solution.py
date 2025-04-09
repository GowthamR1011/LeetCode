class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        
        res = 0
        
        while a or b or c:

            if c & 1 :
                if not (a&1) and not (b&1):
                    res += 1
            else:
                if (a&1):
                    res += 1
                if (b&1):
                    res += 1
            
            a =  a >> 1
            b = b >> 1
            c = c >> 1
        return res