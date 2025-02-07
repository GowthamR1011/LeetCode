class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s = s1
        l,r = 0,0

        while r<len(s2):
            if s2[r] in s:
                s =  s.replace(s2[r],"",1)
                if len(s) == 0:
                    return True
            
            elif s2[r] in s1:
                while s2[r] != s2[l]:
                    s = s + s2[l]
                    l += 1
                l += 1
                
            else:
                l = r + 1
                s = s1
            r += 1
        return False
                