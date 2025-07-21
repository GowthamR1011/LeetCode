class Solution:
    def makeFancyString(self, s: str) -> str:
        
        res = ""
        for ch in s:
            if len(res) > 1 and res[-1] == res[-2] and res[-1] == ch:
                continue
            
            res += ch
        
        return res