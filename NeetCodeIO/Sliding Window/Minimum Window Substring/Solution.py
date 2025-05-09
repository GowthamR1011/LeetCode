class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        counter_t = Counter(t)
        counter = defaultdict(int)
        have, need = 0, len(counter_t)
        res = s + "#"
        l = 0
        for r in range(len(s)):

            counter[s[r]] += 1

            if counter_t[s[r]] == counter[s[r]]:
                have += 1
            
            while have == need:

                if len(res) > (r-l + 1):
                    res = s[l:r+1]
                
                counter[s[l]] -= 1
                if counter_t[s[l]] > counter[s[l]]:
                    have -= 1
                
                l += 1

            r += 1

        return res if len(res) <= len(s) else ""
