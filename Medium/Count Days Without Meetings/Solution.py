class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()
        current_date = 1
        res = 0
        for s,e in meetings:

            if s > current_date:
                res += s - current_date
            
            current_date = max(e+1,current_date)
        
        res += days - current_date + 1
        return res
