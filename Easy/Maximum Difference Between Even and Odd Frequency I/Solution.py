class Solution:
    def maxDifference(self, s: str) -> int:
        
        count = Counter(s)


        max_odd = 0
        min_even = inf


        for ch in count:
            f = count[ch]
            if f % 2 == 0:
                min_even = min(f,min_even)            
            else:
                max_odd = max(f,max_odd)
        
        return max_odd - min_even