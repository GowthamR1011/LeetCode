class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        res = 0
        n = len(startTime)
        i = 0
        prev_end = 0
        left_gap = [0] * n

        prev_start = eventTime
        right_gap = [0] * n

        for i in range(n):
            
            
            l_gap = startTime[i] - prev_end
            
            
            if i == 0:
                left_gap[i] = l_gap
            else:
                left_gap[i] = max(left_gap[i-1], l_gap)
            
            prev_end = endTime[i]

            r = n - i - 1
            r_gap = prev_start - endTime[r]
            if r == n-1:
                right_gap[r] = r_gap
            else:
                right_gap[r] = max(right_gap[r+1], r_gap)


            prev_start = startTime[r]
        

        for i in range(n):
            
            time = endTime[i] - startTime[i]

            if i == 0 :
                if time <= right_gap[i+1]:
                    res = max(res,startTime[i+1])
                else:
                    res = max(res, startTime[i+1] - time)
                
            elif i == n - 1:
                if time <= left_gap[i-1]:
                    res = max(res,eventTime - endTime[i-1])
                else:
                    res = max(res,eventTime - endTime[i-1] - time )
            
            elif time <= left_gap[i-1] or time <= right_gap[i+1]:
                res = max(res,startTime[i+1] - endTime[i-1])
            else:
                res = max(res,startTime[i+1] - endTime[i-1] - time )
                


        return res
        