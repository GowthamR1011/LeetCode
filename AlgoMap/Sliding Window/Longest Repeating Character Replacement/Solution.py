from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        max_w = 0
        max_char_count = 0
        char_count = defaultdict(int)

        while r<len(s):
            
            char_count[s[r]] += 1
            max_char_count = max(max_char_count,char_count[s[r]])
            replacements = r - l + 1 - max_char_count
                
            if replacements > k:
                char_count[s[l]] -= 1
                l = l + 1

            r = r+1 

            
            max_w = max(max_w,r-l)


            
            
            
        
        return max_w
    
