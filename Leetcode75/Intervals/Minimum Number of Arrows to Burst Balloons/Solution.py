class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        prev = points[0][0] - 1
        res = 0
        for a,b in points:

            if prev >= a:
                prev = min(prev,b)
            else:
                res += 1
                prev = b
        
        return res