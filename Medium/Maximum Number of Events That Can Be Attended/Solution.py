class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        max_day = max([e[1] for e in events ])

        n = len(events)
        events.sort()
        h = []
        heapify(h)
        j = 0
        res = 0
        for i in range(1,max_day + 1):

            while j < n and events[j][0] <= i:
                heappush(h,events[j][1])
                j += 1
            
            while h and h[0] < i:
                heappop(h)
            
            if h:
                res += 1
                heappop(h)
        
        return res
            