class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_counter = defaultdict(int)
        t_counter = defaultdict(int)
        for i in range(len(s)):

            s_counter[s[i]] += 1
            t_counter[t[i]] += 1
        
        return s_counter == t_counter
            
        
        

