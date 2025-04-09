class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        start, prev = intervals[0]
        res = 0
        for a,b in intervals[1:]:

            if prev <= a:
                prev = b
            else: 
                prev = min(prev,b)
                res += 1
        
        return res
