class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        n = len(startTime)
        res = 0
        t = 0
        for i in range(n):
            t += endTime[i] - startTime[i]


            l = 0 if i <= k - 1 else endTime[i-k]

            r = startTime[i+1] if i < n-1 else eventTime

            res = max(res, (r-l) - t)

            if i >=k -1:
                t -= endTime[i - k + 1] - startTime[i -k + 1]
        
        return res


        

