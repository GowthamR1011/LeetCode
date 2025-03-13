class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        end = len(s)
        i = 0
        if i == end:
            return True
            
        for ch in t:
            
            
            if s[i] == ch:
                i += 1
                
                if i == end:
                    return True 
                
                
        
        return False