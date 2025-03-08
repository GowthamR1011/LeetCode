class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        last_seen = [-1,-1,-1]
        total = 0

        for i in range(len(s)):
            if s[i] == 'a':
                last_seen[0] = i
            elif s[i] == 'b':
                last_seen[1] = i
            else:
                last_seen[2] = i
            
            if -1 not in last_seen:
                total += 1 + min(last_seen)
        
        return total
    
            