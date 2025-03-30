class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        last = {ch:i for i,ch in enumerate(s)}
        res = []
        
        start = 0
        l,r = 0,0
        while l < len(s):
            r = max(r,last[s[l]])
            if r == l:
                res.append( l - start+ 1)
                start = r + 1
            l += 1
        
        return res
