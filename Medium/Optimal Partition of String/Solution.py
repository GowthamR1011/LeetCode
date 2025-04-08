class Solution:
    def partitionString(self, s: str) -> int:
        
        seen = set()
        res = 0
        for ch in s:

            if ch in seen:
                seen = set([ch])
                res += 1
            else:
                seen.add(ch)
        return res + 1