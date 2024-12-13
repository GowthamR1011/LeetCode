class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0

        val = {"I":1,"V":5,"X":10,"L":50,'C':100,'D':500,'M':1000}
        
        i = len(s) -1

        while i >= 0:
            if i > 0 and val[s[i]] > val[s[i-1]]:
                res += val[s[i]] - val[s[i-1]]
                i -= 1
            else:
                res += val[s[i]]

            
            i -= 1
        
        
        return res